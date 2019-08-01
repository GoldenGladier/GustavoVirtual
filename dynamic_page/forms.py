from django import forms
from .models import Home, Profile
from django.contrib.auth.models import User


class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ('title', 'subtitle',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)

class ContactForm(forms.Form):
    contact_name = forms.CharField(required = True)
    contact_email = forms.EmailField(required = True)
    content = forms.CharField(required = True, widget = forms.Textarea)
