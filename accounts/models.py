from __future__ import unicode_literals
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class UserManage(BaseUserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):

        now = timezone.now()
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('邮箱', unique=True, db_index=True)
    username = models.CharField(
        '用户名', max_length=75, unique=True)
    is_staff = models.BooleanField('职员身份', default=False)
    is_active = models.BooleanField('激活状态', default=True)
    date_joined = models.DateTimeField('注册时间', default=timezone.now)

    login_attempted = models.IntegerField('登录失败几次', default=0)
    update = models.DateTimeField('上次登录尝试', auto_now=True)

    secret = models.CharField('密匙', max_length=16, blank=True)
    verification_needed = models.BooleanField('启用登录验证', default=False)

    objects = UserManage()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    # backend = 'user.backends.AuthenticationBackend'

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        # swappable = 'AUTH_USER_MODEL'

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def activate(self):
        self.is_active = True
        self.save()

    # @property
    # def is_staff(self):
    #     return self.is_admin
