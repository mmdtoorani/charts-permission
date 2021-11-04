from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    # is_staff = forms.BooleanField()
    # is_superuser = forms.BooleanField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]


class LoginForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=None,
    )

    class Meta:
        model = User
        fields = ['username', 'password1', ]
