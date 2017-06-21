from django.conf.urls import url

from . import views


app_name = 'perms'
urlpatterns = [
    url(r'^$', views.PermListView.as_view(), name='list'),
    url(r'^add/$', views.PermCreateView.as_view(), name='add'),
    url(r'^(?P<pk>[0-9]+)/$', views.PermDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/del/$', views.PermDeleteView.as_view(), name='del'),

]
