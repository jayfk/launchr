from django.contrib import admin
from django.urls import path, include

from views import (
    HomeView,
    TermsView,
    PrivacyView,
    SupportView,
    SiteMapView,
    RobotsView
)

urlpatterns = [
    path(
        route='',
        view=HomeView.as_view(),
        name="home"
    ),
    path(
        route='terms-of-service/',
        view=TermsView.as_view(),
        name="tos"
    ),
    path(
        route='privacy-policy/',
        view=PrivacyView.as_view(),
        name="privacy"
    ),
    path(
        route='support/',
        view=SupportView.as_view(),
        name="support"
    ),
    path(
        route='sitemap.xml',
        view=SiteMapView.as_view(),
        name="sitemap"
    ),
    path(
        route='robots.txt',
        view=RobotsView.as_view(),
        name="robots"
    ),
    path(
        route="users/",
        view=include(
            ('users.urls', 'users'),
            namespace="users"
        )
    ),
    path(
        route='stripe/',
        view=include(
            "djstripe.urls",
            namespace="djstripe"
        ),
    ),
    path(
        route='auth/',
        view=include('allauth.urls')
    ),
    path(
        route='admin/',
        view=admin.site.urls,
    ),
]
