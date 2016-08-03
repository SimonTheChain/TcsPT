from django.conf.urls import url
from . import views


app_name = "metadata"


urlpatterns = [

    #  /metadata/
    url(r'^$', views.index, name="index"),

    #  /metadata/metadatas/
    url(r'^metadata/$', views.MetadatasView.as_view(), name="metadatas"),

    #  /metadata/metadata/1/
    url(r'^metadata/(?P<pk>[0-9]+)/$', views.MetadataDetailsView.as_view(), name="metadata_details"),

    #  /metadata/video/add/
    url(r'^metadata/add/$', views.MetadataCreate.as_view(), name="metadata_add"),

    #  /metadata/video/1/update/
    url(r'^metadata/(?P<pk>[0-9]+)/update/$', views.MetadataUpdate.as_view(), name="metadata_update"),

    #  /metadata/video/1/delete/
    url(r'^metadata/(?P<pk>[0-9]+)/delete/$', views.MetadataDelete.as_view(), name="metadata_delete"),

]
