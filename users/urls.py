#!/usr/bin/env python
# coding: utf-8
# Created by guang on 
# 


from django.conf.urls import url

from . import views


app_name = 'users'
urlpatterns = [
    url(r'^$', views.user_list, name='list'),
    url(r'^add/$', views.user_add, name='add'),
    url(r'^(?P<user_id>[0-9]+)/update/$', views.user_update, name='update'),
    url(r'^(?P<user_id>[0-9]+)/$', views.user_detail, name='detail'),
    url(r'^(?P<user_id>[0-9]+)/del/$', views.user_del, name='del'),
    url(r'^login/$', views.login_, name='login'),
    url(r'^logout/$', views.logout_, name='logout'),
]
