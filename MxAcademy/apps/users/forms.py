from django import forms
from captcha.fields import CaptchaField

from MxAcademy.settings import REDIS_HOST, REDIS_PORT
from apps.users.models import UserProfile


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["image"]


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["nick_name", "gender", "birthday", "address"]


class RegisterGetForm(forms.Form):
    captcha = CaptchaField()


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)
