from django import forms
from django.contrib.auth.models import User, Profile
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileForm(forms.ModelForm):
     # This field is for the email, which belongs to the User model
    email = forms.EmailField(required=True)

    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']