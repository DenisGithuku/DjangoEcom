from django import forms
from . import models

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = models.UserModel
        fields = ['username', 'password']


class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.UserModel
        fields = ['username', 'email', 'password']
    

class CheckEmail(forms.ModelForm):
    class Meta:
        model = models.UserModel
        fields = ['email']

class ResetPassword(forms.ModelForm):
    class Meta:
        model = models.UserModel
        fields = ['password']
