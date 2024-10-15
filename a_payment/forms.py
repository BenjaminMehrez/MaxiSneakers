from django.forms import ModelForm
from django import forms
from .models import ShippingAddress


class ShippingAddressForm(ModelForm):
    
    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_state', 'shipping_country']
        exclude = ['user']
        widgets = {
            'shipping_full_name': forms.TextInput(attrs={'placeholder': 'Nombre completo'}, required=True),
            'shipping_email': forms.EmailInput(attrs={'placeholder': 'Correo Electronico'}, required=True),
            'shipping_address1': forms.TextInput(attrs={'placeholder': 'Direccion'}, required=True),
            'shipping_address2': forms.TextInput(attrs={'placeholder': 'Entre Calles'}, required=True),
            'shipping_state': forms.TextInput(attrs={'placeholder': ''}, required=False),
            'shipping_country': forms.TextInput(attrs={'placeholder': 'País'}, required=True),
        }
