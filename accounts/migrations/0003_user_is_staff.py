# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20161128_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='职员身份'),
        ),
    ]
