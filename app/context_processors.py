from typing import Dict

from django.conf import settings
from django.http.request import HttpRequest


def plan_context(request: HttpRequest) -> Dict:
    """Adds all configured plans to the template context"""
    return {
        "plans": settings.PLANS
    }


def base_url_context(request: HttpRequest) -> Dict:
    """Adds the base url (protocol://host) to the template context"""
    return {
        "base_url": request.build_absolute_uri("/")[:-1]
    }


def stripe_context(request: HttpRequest) -> Dict:
    """Adds the configured stripe public key to the template context"""
    return {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    }
