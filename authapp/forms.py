from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email",
                  "username", )
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "username": "Username",
            "email": "Email",
            # "password1": "Password",
            # "password2": "Confirm Password"
            # "profile_picture": "Upload Profile Picture"
        }

    password = forms.CharField(max_length=150, label="Password",
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(max_length=150, label="Confirm Password",
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))

    def __init__(self, *args, **kwargs) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data["password"]
        password2 = cleaned_data["password2"]

        if len(password) < 6:
            self.errors['password'] = 'Password should be at least 6 characters'
            # return forms.ValidationError("Password should be at least 6 characters.")

        if password != password2:
            self.errors['password2'] = 'Passwords did not match'
            # return forms.ValidationError("Password should be at least 6 characters.")

        return cleaned_data

    def save(self, commit=True) -> Any:
        try:
            password = self.cleaned_data["password"]
            user = super().save(commit=False)
            user.set_password(password)
            user.is_staff = True
            print(password)
            if commit:
                user.save()

            return user

        except Exception as ex:
            print(ex.args[0])
            print("Hello")
            # print(dict(ex)["field"])
            # self.errors[dict(ex)["field"][0]] = str(dict(ex)["message"][0])


class SignInForm(forms.Form):
    username_or_email = forms.CharField(
        label="Username or Email", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
