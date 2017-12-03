from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Static pages
    url(r'^$', views.index, name='index'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^howtosetup/$', views.howtosetup, name='howtosetup'),
    url(r'^dbsave/',views.dbSave, name='dbSave'),

    # Form pages
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^server/$',views.server,name='server'),

    # Detail pages
    url(r'^serverdetail/(?P<pk>[0-9]+)/$', views.server_detail, name='server_detail'),
    url(r'^ramchart/(?P<pk>[0-9]+)/$', views.ram_chart, name='ram_chart'),
    url(r'^cpuchart/(?P<pk>[0-9]+)/$', views.cpu_chart, name='cpu_chart'),
    url(r'^diskchart/(?P<pk>[0-9]+)/$', views.disk_chart, name='disk_chart'),
    url(r'^chart/(?P<pk>[0-9]+)/$', views.chart, name='chart'),

    # For Development
    url(r'^user$',views.checkUser,name='checkUser'),
]
