from django.conf.urls import url

from . import views


app_name = 'perm'
urlpatterns = [
    url(r'^$', views.perm_list, name='list'),
    url(r'^add/$', views.perm_add, name='add'),
    url(r'^detail/(\d+)/$', views.perm_detail, name='detail'),
    url(r'^recycle/$', views.perm_recycle, name='recycle'),

]
