from django import forms
from django.contrib.auth.models import User
from basicApp.models import UserProfileInfo

class UserInfo(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','password','email')


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')

