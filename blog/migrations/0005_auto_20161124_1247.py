# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161119_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='标签')),
            ],
            options={
                'verbose_name_plural': '文章标签',
                'verbose_name': '文章标签',
            },
        ),
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='标签'),
        ),
    ]
