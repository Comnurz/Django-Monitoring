from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ramdata/',views.ramData, name='ramData'),
    url(r'^dbsave/',views.dbSave, name='dbSave'),
    # url(r'^cpudata/$',views.cpuData, name='cpuData'),
    # url(r'^diskdata/$',views.diskData, name='diskData'),
]
