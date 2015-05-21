__author__ = 'zhangxg'

from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r"^chart/$", views.index, name='index'),
    url(r"^dashboard/$", views.load_dash_board),
    url(r"^dashboard/search/$", views.search),
    url(r"^dashboard/detail/(.+)/$", views.show_detail),

    # url(r"^chart/disc/$", views.index, name='disc'),
    # url(r"^chart/disc/detail/$", views.getdata, name='getdata'),
    # url(r"^chart/disc/(.+)/$", views.getDiscInfoByPara, name='disc'),
    #
    #
    # url(r"^tryajax/$", views.tryAjax, name='disc'),
    # url(r"^tryajax/getdata/$", views.getdata, name='disc'),
    # url(r"^chart/disc/(.+)/$", views.getDiscInfoByPara, name='disc'),
]