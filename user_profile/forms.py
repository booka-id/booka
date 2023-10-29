from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class RegisterForm(UserCreationForm):

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        profile_pic = self.cleaned_data.get("profile_pic")
        if profile_pic:
            user.profile_pic = profile_pic

        if commit:
            user.save()

        return user

    class Meta:
        model = User
        fields= ["email", "username", "profile_pic","first_name", "last_name"]

class ChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields= ["email", "username", "profile_pic", "first_name", "last_name"]
