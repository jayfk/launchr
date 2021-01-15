from allauth.account.forms import SignupForm
from django import forms

from users.models import User


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user


class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'newsletter',
        )
