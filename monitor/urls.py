from django.urls import re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Static pages
    re_path(r'^detail/$', views.detail, name='detail'),
    re_path(r'^howtosetup/$', views.howtosetup, name='howtosetup'),
    re_path(r'^dashboard/$', views.dashboard, name='dashboard'),

    # Form pages
    re_path(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^server/$', views.server, name='server'),

    # Detail pages
    re_path(r'^serverdetail/(?P<pk>[0-9]+)/$', views.server_detail,
            name='server_detail'),
    re_path(r'^ramchart/(?P<pk>[0-9]+)/$', views.ram_chart, name='ram_chart'),
    re_path(r'^cpuchart/(?P<pk>[0-9]+)/$', views.cpu_chart, name='cpu_chart'),
    re_path(r'^diskchart/(?P<pk>[0-9]+)/$', views.disk_chart, name='disk_chart'),
    re_path(r'^chart/(?P<pk>[0-9]+)/$', views.chart, name='chart'),

    # Example pages
    re_path(r'^exampleramchart/', views.example_ram_chart,
            name='example_ram_chart'),
    re_path(r'^examplecpuchart/', views.example_cpu_chart,
            name='example_cpu_chart'),
    re_path(r'^examplediskchart/', views.example_disk_chart,
            name='example_disk_chart'),
    re_path(r'^examplechart/', views.example_chart, name='example_chart'),
    re_path(r'^exampledashboard/', views.example_dashboard,
            name='example_dashboard'),
    re_path(r'^exampledetail/', views.example_detail, name='example_detail'),
    re_path(r'^exampleserverdetail/', views.example_server_detail,
            name='example_server_detail'),
    re_path(r'^exampleserver2detail/', views.example_server2_detail,
            name='example_server2_detail'),
    re_path(r'^exampleserver/', views.example_server, name='example_server'),
    re_path(r'^examplehowtosetup/', views.example_howtosetup,
            name='example_howtosetup'),


    # API
    re_path(r'^api/register/$', views.register_token, name='registerToken'),
    re_path(r'^api/dbsave/$', views.db_save, name='dbSave'),


    re_path(r'^$', views.index, name='index'),
]
