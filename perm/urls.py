from django.conf.urls import url

from . import views


app_name = 'perm'
urlpatterns = [
    url(r'^$', views.perm_list),
]
