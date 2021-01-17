import json

import stripe
from allauth.account.views import (
    PasswordChangeView as AllauthPasswordChangeView,
    EmailView as AllauthEmailView,
)
from allauth.account.adapter import get_adapter
from allauth.account import signals
from allauth.account.models import EmailAddress
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, UpdateView
from djstripe.models import Customer
from users.forms import AccountForm
from users.email import subscribe_to_mailing_list, unsubscribe_from_mailing_list

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "users/dashboard.html"


class AccountView(LoginRequiredMixin, UpdateView):
    template_name = "users/account.html"
    form_class = AccountForm

    def get_success_url(self):
        return reverse("users:account")

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        data = super(AccountView, self).get_context_data(**kwargs)
        data['password_changed'] = bool(self.request.GET.get("password_changed", False))
        data['email_changed'] = bool(self.request.GET.get("email_changed", False))
        return data


class PasswordChangeView(AllauthPasswordChangeView):

    def get_success_url(self):
        return reverse("users:account") + "?password_changed=True"


class EmailChangeView(AllauthEmailView):

    def form_valid(self, form):
        # copying allauths form validation to be
        # as close to the original as possible.
        # we could remove the signals since we are not using them,
        # but I left them in if we need them at some point
        email_address = form.save(self.request)
        get_adapter(self.request).add_message(
            self.request,
            messages.INFO,
            "account/messages/" "email_confirmation_sent.txt",
            {"email": form.cleaned_data["email"]},
        )
        signals.email_added.send(
            sender=self.request.user.__class__,
            request=self.request,
            user=self.request.user,
            email_address=email_address,
        )
        # make the email address primary
        email_address.set_as_primary()
        # subscribe the user to the mailing list, if it is enabled
        if self.request.user.newsletter:
            subscribe_to_mailing_list(
                email=email_address.email,
                first=self.request.user.first_name,
                last=self.request.user.last_name
            )
        # get all old email addresses for this user and delete them
        # from the database and from the mailing list
        for email in EmailAddress.objects.filter(
            user=self.request.user
        ).exclude(
            pk=email_address.pk
        ):
            unsubscribe_from_mailing_list(
                email=email.email
            )
            email.delete()
        return super(EmailChangeView, self).form_valid(form)

    def get_success_url(self):
        # on a successfull email change, we are going to redirect
        # the user to the main account page
        return reverse("users:account") + "?email_changed=True"

    def post(self, request, *args, **kwargs):
        # overriding the default post method to disable all
        # the add/remove/send/primary actions here.
        # we are going to handle them in form_valid
        return super(AllauthEmailView, self).post(request, *args, **kwargs)


class SubscriptionView(LoginRequiredMixin, TemplateView):
    template_name = "users/subscription.html"


class BillingView(LoginRequiredMixin, UpdateView):

    def post(self, request, *args, **kwargs):
        url = self.request.POST.get("url", False)
        if not url:
            url = self.request.build_absolute_uri(settings.LOGIN_REDIRECT_URL)

        customer, created = Customer.get_or_create(request.user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        response = stripe.billing_portal.Session.create(
            customer=customer.id,
            return_url=url,
        )
        return redirect(to=response.url, permanent=False)

    def get(self, request, *args, **kwargs):
        raise PermissionDenied


class CheckoutView(LoginRequiredMixin, UpdateView):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        plan_id = data.get("priceId", False)

        if not plan_id:
            raise PermissionDenied

        customer, created = Customer.get_or_create(request.user)

        stripe.api_key = settings.STRIPE_SECRET_KEY

        url = f"{self.request.scheme}://{self.request.get_host()}/"
        session = stripe.checkout.Session.create(
            customer=customer.id,
            payment_method_types=['card'],
            line_items=[{
                'price': plan_id,
                'quantity': 1,
            }],
            mode='subscription',
            success_url=url,
            cancel_url=url,
        )
        return JsonResponse({"id": session['id']})

    def get(self, request, *args, **kwargs):
        raise PermissionDenied
