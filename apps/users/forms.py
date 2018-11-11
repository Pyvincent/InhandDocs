########################################################################################################################
## Django 自带模块导入
########################################################################################################################
from django import forms
from captcha.fields import CaptchaField

########################################################################################################################
## 系统自带模块导入
########################################################################################################################


########################################################################################################################
## 自建模块导入
########################################################################################################################
from apps.users.models import *


########################################################################################################################
## 登陆表单
########################################################################################################################
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=4, required=True)
    password = forms.CharField(max_length=20, min_length=6, required=True)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误!'})


########################################################################################################################
## 忘记密码表单
########################################################################################################################
class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(required=True)


########################################################################################################################
## 重置密码表单
########################################################################################################################
class ResetPasswordForm(forms.Form):
    password1 = forms.CharField(min_length=6, max_length=16, required=True)
    password2 = forms.CharField(min_length=6, max_length=16, required=True)


########################################################################################################################
## 修改用户信息表单
########################################################################################################################
class ChangeUserInfoForm(forms.Form):
    address = forms.CharField(max_length=200, required=True)
    # birthday = forms.DateField(required=True)
    gender = forms.CharField(required=True)
    mobile = forms.CharField(max_length=12, required=True)
    qq = forms.CharField(max_length=12, required=True)
    wechat = forms.CharField(max_length=20, required=True)
    desc = forms.Textarea()


########################################################################################################################
## 修改用户头像
########################################################################################################################
class ChangeAvatarForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']


########################################################################################################################
## 修改密码表单
########################################################################################################################
class ChangePasswordForm(forms.Form):
    password1 = forms.CharField(min_length=6, max_length=16, required=True)
    password2 = forms.CharField(min_length=6, max_length=16, required=True)
