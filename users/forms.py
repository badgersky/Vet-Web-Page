from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from . import models


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'name': 'username',
            'placeholder': 'username',
        })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'name': 'password',
            'placeholder': 'password',
        })
    )

    class Meta:
        fields = ('username', 'password')

    error_messages = {
        'invalid_login': 'Email or password don`t match any user.'
    }


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'name': 'password',
            'placeholder': 'password',
        })
    )
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'name': 'confirm_password',
            'placeholder': 'confirm_password',
        })
    )

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name', 'password', 'confirm_password')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        validate_password(confirm_password, get_user_model())

        if password and confirm_password and confirm_password != password:
            raise ValidationError(f'Passwords don`t match')

        return confirm_password

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if models.CustomUser.objects.filter(email=email).exists():
            raise ValidationError(f'Try using different email')

        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if models.CustomUser.objects.filter(username=username).exists():
            raise(ValidationError(f'Try using different username'))

        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        user.is_active = True

        if commit:
            user.save()

        return user
