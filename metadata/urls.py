from django.conf.urls import url
from . import views


app_name = "metadata"


urlpatterns = [

    #  /metadata/
    url(r'^$', views.index, name="index"),

    #  /metadata/metadata/xml_raw/download
    url(r'^metadata/(?P<pk>[0-9]+)/xml_raw/download/$', views.download_raw_xml, name="download_raw_xml"),

    #  /metadata/metadata/xml_itunes/download
    url(r'^metadata/(?P<pk>[0-9]+)/xml_itunes/download/$', views.download_itunes_xml, name="download_itunes_xml"),

    #  /metadata/metadatas/
    url(r'^metadata/$', views.MetadatasView.as_view(), name="metadatas"),

    #  /metadata/metadata/1/
    url(r'^metadata/(?P<pk>[0-9]+)/$', views.MetadataDetailsView.as_view(), name="metadata_details"),

    #  /metadata/metadata/add/
    url(r'^metadata/add/$', views.MetadataCreate.as_view(), name="metadata_add"),

    #  /metadata/metadata/1/update/
    url(r'^metadata/(?P<pk>[0-9]+)/update/$', views.MetadataUpdate.as_view(), name="metadata_update"),

    #  /metadata/metadata/1/general/
    url(r'^metadata/(?P<pk>[0-9]+)/general/$', views.MetadataGeneral.as_view(), name="metadata_general"),

    #  /metadata/metadata/1/itunes/
    url(r'^metadata/(?P<pk>[0-9]+)/itunes/$', views.MetadataItunes.as_view(), name="metadata_itunes"),

    #  /metadata/metadata/1/sasktel/
    url(r'^metadata/(?P<pk>[0-9]+)/sasktel/$', views.MetadataSasktel.as_view(), name="metadata_sasktel"),

    #  /metadata/metadata/1/delete/
    url(r'^metadata/(?P<pk>[0-9]+)/delete/$', views.MetadataDelete.as_view(), name="metadata_delete"),

]
