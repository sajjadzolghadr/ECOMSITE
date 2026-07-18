from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [ "full_name","email","phone","address",]

        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": "form-control mb-3",
                "placeholder": "Full Name",
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control mb-3",
                "placeholder": "Email Address",
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control mb-3",
                "placeholder": "Phone Number",
            }),

            "address": forms.Textarea(attrs={
                "class": "form-control mb-3",
                "rows": 4,
                "placeholder": "Shipping Address",
            }),
        }