import json

import stripe
from allauth.account.views import PasswordChangeView as AllauthPasswordChangeView
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, UpdateView
from djstripe.models import Customer
from users.forms import AccountForm


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
        return data


class PasswordChangeView(AllauthPasswordChangeView):

    def get_success_url(self):
        return reverse("users:account") + "?password_changed=True"


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
