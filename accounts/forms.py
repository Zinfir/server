from django import forms
import random, hashlib
from accounts.models import Account


class Account_Form(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'phone',
            'avatar'
            ]
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'field_password'}),
            'email': forms.EmailInput(attrs={'class': 'field_email'}),
        }


class Registration_Form(forms.Form):
    username = forms.CharField(
        label='Login', max_length=150,
        widget=forms.widgets.TextInput(
            attrs={'class': 'field_username'}
        )
    )
    email = forms.CharField(
        max_length=150, required=True,
        widget=forms.widgets.EmailInput(
            attrs={'class': 'field_email'}
        )
    )
    password = forms.CharField(
        max_length=250,
        widget=forms.widgets.PasswordInput(
            attrs={'class': 'field_password'}
        )
    )
    password_confirm = forms.CharField(
        max_length=250,
        widget=forms.widgets.PasswordInput(
            attrs={'class': 'field_password'}
        )
    )


class Registration_Model_Form(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'username',
            'password',
            'email',
            ]
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'field_password'}),
            'email': forms.EmailInput(attrs={'class': 'field_email'}),
        }