from __future__ import unicode_literals
from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import ugettext, ugettext_lazy as _
from accounts.models import User


class LoginForm(forms.Form):
    """用户登录"""
    email = forms.EmailField(error_messages={
        'required': '请输入注册邮箱',
        'invalid': '请输入正确的邮箱',
        'max_length': '邮箱名超长'
    })

    password = forms.CharField(widget=forms.PasswordInput(render_value=False), min_length=6, error_messages={
        'required': '请输入登录密码',
        'invalid': 'password',
        'min_length': '密码长度不能小于6位'
    })

    user = None

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        self.user = authenticate(email=cleaned_data.get('email'),
                                 password=cleaned_data.get('password'))

        if not self.user:
            raise forms.ValidationError('用户名或用户密码不正确')
        if not self.user.is_active:
            raise forms.ValidationError('账号尚未激活或锁定')

        return cleaned_data
