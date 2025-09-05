# donations/forms.py
from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=True,
        label="Mobile Banking Password"
    )

    class Meta:
        model = Donation
        fields = ['name', 'batch', 'method', 'amount', 'mobile']

class OTPForm(forms.Form):
    mobile = forms.CharField(max_length=20, widget=forms.HiddenInput())
    otp = forms.CharField(max_length=6, required=True)
