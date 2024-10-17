from django.forms import ModelForm
from django import forms
from .models import ShippingAddress


class ShippingAddressForm(ModelForm):
    
    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_state', 'shipping_country']
        exclude = ['user']
        widgets = {
            'shipping_full_name': forms.TextInput(attrs={'placeholder': 'Nombre completo'}),
            'shipping_email': forms.EmailInput(attrs={'placeholder': 'Correo Electronico'}),
            'shipping_address1': forms.TextInput(attrs={'placeholder': 'Direccion'}),
            'shipping_address2': forms.TextInput(attrs={'placeholder': 'Entre Calles'}),
            'shipping_state': forms.TextInput(attrs={'placeholder': 'Estado'}),
            'shipping_country': forms.TextInput(attrs={'placeholder': 'País'}),
        }
