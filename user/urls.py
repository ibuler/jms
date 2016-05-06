#!/usr/bin/env python
# coding: utf-8
# Created by guang on 
# 


from django.conf.urls import url

from . import views


app_name = 'user'
urlpatterns = [
    url(r'^add/$', views.user_add, name='add'),
    url(r'^list/$', views.user_list, name='list'),
]
