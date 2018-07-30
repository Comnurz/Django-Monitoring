from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    # Static pages
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^howtosetup/$', views.howtosetup, name='howtosetup'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),

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

    # Example pages
    url(r'^exampleramchart/', views.example_ram_chart, name='example_ram_chart'),
    url(r'^examplecpuchart/', views.example_cpu_chart, name='example_cpu_chart'),
    url(r'^examplediskchart/', views.example_disk_chart, name='example_disk_chart'),
    url(r'^examplechart/', views.example_chart, name='example_chart'),
    url(r'^exampledashboard/', views.example_dashboard, name='example_dashboard'),
    url(r'^exampledetail/', views.example_detail, name='example_detail'),
    url(r'^exampleserverdetail/', views.example_server_detail, name='example_server_detail'),
    url(r'^exampleserver2detail/', views.example_server2_detail, name='example_server2_detail'),
    url(r'^exampleserver/', views.example_server, name='example_server'),
    url(r'^examplehowtosetup/', views.example_howtosetup, name='example_howtosetup'),


    # For Development
    url(r'^dbsave/',views.db_save, name='dbSave'),
    url(r'^user$',views.check_user,name='checkUser'),
    url(r'^delete/(?P<pk>[0-9]+)/$',views.delete_server,name='deleteServer'),


    url(r'^$', views.index, name='index'),
]
