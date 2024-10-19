from django.forms import ModelForm
from django import forms
from .models import ShippingAddress


class ShippingAddressForm(ModelForm):
    
    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_address', 'shipping_street', 'shipping_zipcode', 'shipping_city', 'shipping_country']
        exclude = ['user']
        widgets = {
            'shipping_full_name': forms.TextInput(attrs={'placeholder': 'Nombre completo'}),
            'shipping_email': forms.EmailInput(attrs={'placeholder': 'Correo Electronico'}),
            'shipping_address': forms.TextInput(attrs={'placeholder': 'Direccion'}),
            'shipping_street': forms.TextInput(attrs={'placeholder': 'Calle y número'}),
            'shipping_zipcode': forms.TextInput(attrs={'placeholder': 'Condigo Postal'}),
            'shipping_city': forms.TextInput(attrs={'placeholder': 'Provincia'}),
            'shipping_country': forms.TextInput(attrs={'placeholder': 'País'}),
        }
        labels = {
            'shipping_full_name': 'Nombre completo',
            'shipping_email': 'Correo Electrónico',
            'shipping_address': 'Dirección',
            'shipping_street': 'Calle y número',
            'shipping_zipcode': 'Condigo Postal',
            'shipping_state': 'Provincia',
            'shipping_country': 'País',
        }
