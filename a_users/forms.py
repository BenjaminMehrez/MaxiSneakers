from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'first_name', 'last_name', 'phone', 'location']
        widgets = {
            'image': forms.FileInput(),
            'first_name' : forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name' : forms.TextInput(attrs={'placeholder': 'Last name'}),
            'phone' : forms.TextInput(attrs={'placeholder': 'Add your phone'}),
            'location' : forms.Textarea(attrs={'rows':3, 'placeholder': 'Add Location'}),
        }
        
        
class EmailForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email']