__author__ = 'zhangxg'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^dashboard/$", views.show_dashboard),
    url(r"^dashboard/tenants_stats/$", views.get_tenants_stats),
    url(r"^dashboard/cpu/$", views.get_cpu),
    url(r"^dashboard/memory/$", views.get_memory),
    url(r"^dashboard/disk_read/$", views.get_disk_read),
    url(r"^dashboard/disk_write/$", views.get_disk_write),
    url(r"^dashboard/network_in/$", views.get_network_in),
    url(r"^dashboard/network_out/$", views.get_network_out),

    url(r"^dashboard/tenants_vm_env/$", views.get_tenants_vm_dist_by_env),
    url(r"^dashboard/search/$", views.search),
    url(r"^dashboard/detail/(.+)/$", views.show_detail),

    url(r"^dashboard/tenents/$", views.load_dash_board),
    url(r"^dashboard/tenents/get/$", views.get_tenents),
    url(r"^dashboard/tenents/(.+)/$", views.get_tenent_detail),
]