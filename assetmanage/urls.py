from django.conf.urls import url
from . import views


app_name = "assetmanage"


urlpatterns = [

    #  /assetmanage/
    url(r'^$', views.index, name="index"),

    #  /assetmanage/asset/select/
    url(r'^asset/select/$', views.asset_select, name="asset_select"),

    #  /assetmanage/video/xml/download
    url(r'^video/(?P<pk>[0-9]+)/xml/download/$', views.download_video_xml, name="download_video_xml"),

    #  /assetmanage/videos/
    url(r'^videos/$', views.VideosView.as_view(), name="videos"),

    #  /assetmanage/video/1/
    url(r'^video/(?P<pk>[0-9]+)/$', views.VideoDetailsView.as_view(), name="video_details"),

    #  /assetmanage/video/add/
    url(r'^video/add/$', views.VideoCreate.as_view(), name="video_add"),

    #  /assetmanage/video/1/update/
    url(r'^video/(?P<pk>[0-9]+)/update/$', views.VideoUpdate.as_view(), name="video_update"),

    #  /assetmanage/video/1/delete/
    url(r'^video/(?P<pk>[0-9]+)/delete/$', views.VideoDelete.as_view(), name="video_delete"),

]
