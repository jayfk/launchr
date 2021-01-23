from .base import *

########################################
# PAYMENTS
########################################
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

########################################
# SECURITY
########################################
ALLOWED_HOSTS = ["*"]

########################################
# PAYMENTS
########################################
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY")
STRIPE_TEST_SECRET_KEY = STRIPE_SECRET_KEY
STRIPE_TEST_PUBLIC_KEY = STRIPE_PUBLIC_KEY
STRIPE_LIVE_MODE = False
DJSTRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET")
# todo: update your plans here
# use the stripe dashboard to create plans for this project,
# then fill them in here attach them to your app
# To configure payments, take a look at: https://getlaunchr.com/docs/payments/
PLANS["starter"]['stripe_id'] = ''
PLANS["basic"]['stripe_id'] = ''
PLANS["pro"]['stripe_id'] = ''
TRIAL_PLAN_KEY = 'pro'
# Bypassing Stripe allows us to test the app without setting
# up Stripe for every development environment. Don't use this
# in production.
BYPASS_STRIPE = True

########################################
# CAPTCHA
########################################
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
