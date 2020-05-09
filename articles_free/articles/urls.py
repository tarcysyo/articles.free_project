from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    #re_path(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    #re_path(r'^(?P<slug>[\w_-]+)/$', views.detail, name='detail'),
    re_path(r'^publicar/$', views.publication, name='publication'),
]