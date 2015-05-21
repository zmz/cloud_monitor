__author__ = 'zhangxg'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^dashboard/$", views.load_dash_board),
    url(r"^dashboard/search/$", views.search),
    url(r"^dashboard/detail/(.+)/$", views.show_detail),
]