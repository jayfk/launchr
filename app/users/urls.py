from django.urls import path

from .views import (
    DashboardView,
    AccountView,
    PasswordChangeView,
    BillingView,
    CheckoutView,
    SubscriptionView,
EmailChangeView,
)

urlpatterns = [
    path(
        route='',
        view=DashboardView.as_view(),
        name="dashboard"
    ),
    path(
        route='account/',
        view=AccountView.as_view(),
        name="account"
    ),
    path(
        route='account/change-password/',
        view=PasswordChangeView.as_view(),
        name="change-password"
    ),
    path(
        route='account/change-email/',
        view=EmailChangeView.as_view(),
        name="change-email"
    ),
    path(
        route='subscription/',
        view=SubscriptionView.as_view(),
        name="subscription"
    ),
    path(
        route='billing/',
        view=BillingView.as_view(),
        name='billing'
    ),
    path(
        route='checkout/',
        view=CheckoutView.as_view(),
        name="checkout"
    ),
]
