from django import forms

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
