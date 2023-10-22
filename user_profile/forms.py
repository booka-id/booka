from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields= ["email", "username", "first_name", "last_name"]

class ChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields= ["email", "username", "profile_pic", "first_name", "last_name"]
