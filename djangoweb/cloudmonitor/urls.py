__author__ = 'zhangxg'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^chart/$", views.index, name='index'),
    url(r"^chart/disc/$", views.getDiscInfo, name='disc'),
]