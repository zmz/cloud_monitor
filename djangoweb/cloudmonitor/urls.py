__author__ = 'zhangxg'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^dashboard/$", views.show_dashboard),
    url(r"^dashboard/cpu/$", views.get_cpu),
    url(r"^dashboard/search/$", views.search),
    url(r"^dashboard/detail/(.+)/$", views.show_detail),

    url(r"^dashboard/tenents/$", views.load_dash_board),
    url(r"^dashboard/tenents/get/$", views.get_tenents),
    url(r"^dashboard/tenents/(.+)/$", views.get_tenent_detail),
]