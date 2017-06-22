#!/usr/bin/env python
# coding: utf-8
# Created by guang on
#

from django.conf.urls import url

from . import views


app_name = 'assets'
urlpatterns = [
    url(r'^$', views.AssetListView.as_view(), name='list'),
    url(r'^add/$', views.AssetCreateView.as_view(), name='add'),
    url(r'^(?P<pk>[0-9]+)/del/$', views.AssetDeleteView.as_view(), name='del'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.AssetUpdateView.as_view(), name='update'),
]
