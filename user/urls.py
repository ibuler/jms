#!/usr/bin/env python
# coding: utf-8
# Created by guang on 
# 


from django.conf.urls import url

from . import views


app_name = 'user'
urlpatterns = [
    url(r'^$', views.user_list, name='list'),
    url(r'^add/$', views.user_add, name='add'),
    url(r'^del/$', views.user_del, name='del'),
    url(r'^login/$', views.login_, name='login'),
    url(r'^logout/$', views.logout_, name='logout'),
]
