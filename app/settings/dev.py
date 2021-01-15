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
# todo: use the stripe dashboard to create the plans for this project,
# todo: then fill them in here
PLANS["starter"]['stripe_id'] = ''
PLANS["basic"]['stripe_id'] = ''
PLANS["pro"]['stripe_id'] = ''
TRIAL_PLAN_KEY = 'pro'

########################################
# CAPTCHA
########################################
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
