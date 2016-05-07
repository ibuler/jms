#!/usr/bin/env python
# coding: utf-8
# Created by guang on 
# 

from django.conf.urls import url

from . import views


app_name = 'asset'
urlpatterns = [
    url(r'^$', views.asset_list, name='list'),
    url(r'^add/$', views.asset_add, name='add'),
    url(r'^del/$', views.asset_del, name='del'),
]
