"""
Django base settings file for dev and prod.
"""
import os
from pathlib import Path

from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

########################################
# APPS
########################################
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    'allauth',
    'allauth.account',
    'djstripe',
    'captcha',
    'users',
]

########################################
# MIDDLEWARE
########################################
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

########################################
# SECURITY
########################################
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = bool(os.getenv("DJANGO_DEBUG", "False").lower() in ["true", "1"])
ALLOWED_HOSTS = []

########################################
# OTHER
########################################
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'
SITE_ID = 1

########################################
# TEMPLATES
########################################
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'context_processors.plan_context',
                'context_processors.base_url_context',
                'context_processors.stripe_context',
            ],
        },
    },
]

########################################
# DATABASE
########################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_DB"),
        'USER': os.environ.get("POSTGRES_USER"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

########################################
# PASSWORD VALIDATION
########################################
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

########################################
# INTERNATIONALISATION
########################################
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

########################################
# STATIC SETTINGS
########################################
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

########################################
# AUTHENTICATION
########################################
AUTH_USER_MODEL = 'users.User'
AUTHENTICATION_BACKENDS = (
    "allauth.account.auth_backends.AuthenticationBackend",
)
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_FORMS = {'signup': 'users.forms.CustomSignupForm'}
ACCOUNT_EMAIL_SUBJECT_PREFIX = ""
LOGIN_REDIRECT_URL = reverse_lazy("users:dashboard")
LOGIN_URL = reverse_lazy("account_login")

########################################
# SITE SETTINGS
########################################
# todo: set your site name, your country and your support email here
SITE_NAME = "launchr"
SITE_LOCATION = "United States"
SUPPORT_EMAIL = "support@example.com"

########################################
# PAYMENTS
########################################
TRIAL_PLAN_STRIPE_ID = None
DJSTRIPE_USE_NATIVE_JSONFIELD = True
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"
# todo: set your trial length here
TRIAL_DAYS = 14
# todo: update your plans according to your needs
PLANS = {
    "starter": {
        "name": "Starter",
        "stripe_id": None,
        "available": True,
        "price": "4.99",
        "features": [
            {
                "enabled": True,
                "text": "Feature 1",
                "key": "feature_1"
            },
            {
                "enabled": False,
                "text": "Feature 2",
                "key": "feature_2"
            },
            {
                "enabled": False,
                "text": "Feature 3",
                "key": "feature_3"
            },
            {
                "enabled": False,
                "text": "Feature 4",
                "key": "feature_4"
            },
        ]
    },
    "basic": {
        "name": "Basic",
        "stripe_id": None,
        "available": True,
        "price": "9.99",
        "features": [
            {
                "enabled": True,
                "text": "Feature 1",
                "key": "feature_1"
            },
            {
                "enabled": True,
                "text": "Feature 2",
                "key": "feature_2"
            },
            {
                "enabled": False,
                "text": "Feature 3",
                "key": "feature_3"
            },
            {
                "enabled": False,
                "text": "Feature 4",
                "key": "feature_4"
            },
        ]
    },
    "pro": {
        "name": "Pro",
        "stripe_id": None,
        "available": True,
        "price": "19.99",
        "features": [
            {
                "enabled": True,
                "text": "Feature 1",
                "key": "feature_1"
            },
            {
                "enabled": True,
                "text": "Feature 2",
                "key": "feature_2"
            },
            {
                "enabled": True,
                "text": "Feature 3",
                "key": "feature_3"
            },
            {
                "enabled": True,
                "text": "Feature 4",
                "key": "feature_4"
            },
        ]
    }
}
