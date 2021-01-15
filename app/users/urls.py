from django.urls import path

from .views import (
    DashboardView,
    AccountView,
    PasswordChangeView,
    BillingView,
    CheckoutView,
    SubscriptionView,
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
