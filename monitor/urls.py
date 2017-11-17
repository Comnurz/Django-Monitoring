from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.server_detail, name='server_detail'),
    url(r'^howtosetup/$', views.howtosetup, name='howtosetup'),
    url(r'^dbsave/',views.dbSave, name='dbSave'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^server/$',views.server,name='server'),
    url(r'^user$',views.checkUser,name='checkUser')
]
