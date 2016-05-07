# coding: utf-8

from django.db import models

from django.contrib.auth.models import User
from asset.models import Asset
# Create your models here.


class Perm(models.Model):
    user = models.ManyToManyField(User, verbose_name='用户')
    asset = models.ManyToManyField(Asset, verbose_name='资产')
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
