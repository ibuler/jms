from django.conf.urls import url

from . import views


app_name = 'perm'
urlpatterns = [
    url(r'^$', views.perm_list, name='list'),
    url(r'^add/$', views.perm_add, name='add'),
]
