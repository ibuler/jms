# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(unique=True, verbose_name='IP')),
                ('port', models.IntegerField(default=22, verbose_name='端口')),
                ('username', models.CharField(max_length=20, verbose_name='管理用户名')),
                ('password', models.CharField(max_length=32, verbose_name='管理密码')),
                ('os', models.CharField(choices=[('C', 'CentOS'), ('U', 'Ubuntu'), ('D', 'Debian'), ('R', 'Redhat'), ('B', 'BSD')], max_length=2, verbose_name='系统平台')),
                ('is_active', models.BooleanField(default=True, verbose_name='激活')),
            ],
        ),
    ]
