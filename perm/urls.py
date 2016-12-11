from django.conf.urls import url

from . import views


app_name = 'perm'
urlpatterns = [
    url(r'^$', views.perm_list, name='list'),
    url(r'^add/$', views.perm_add, name='add'),
    url(r'^(?P<perm_id>[0-9]+)/$', views.perm_detail, name='detail'),
    url(r'^recycle/$', views.perm_recycle, name='recycle'),
    url(r'^(?P<perm_id>[0-9]+)/del/$', views.perm_del, name='del'),
]
