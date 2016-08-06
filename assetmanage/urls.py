from django.conf.urls import url
from . import views


app_name = "assetmanage"


urlpatterns = [

    #  /assetmanage/
    url(r'^$', views.index, name="index"),

    #  /assetmanage/asset/select/
    url(r'^asset/select/$', views.asset_select, name="asset_select"),

    #  /asset/add/xml/
    url(r'^asset/add/xml/$', views.upload_xml, name="asset_add_xml"),

    #  /assetmanage/video/xml/download
    url(r'^video/(?P<pk>[0-9]+)/xml/download/$', views.download_video_xml, name="download_video_xml"),

    #  /assetmanage/audio/xml/download
    url(r'^audio/(?P<pk>[0-9]+)/xml/download/$', views.download_audio_xml, name="download_audio_xml"),
    
    #  /assetmanage/subtitle/xml/download
    url(r'^subtitle/(?P<pk>[0-9]+)/xml/download/$', views.download_subtitle_xml, name="download_subtitle_xml"),

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

    #  /assetmanage/audios/
    url(r'^audios/$', views.AudiosView.as_view(), name="audios"),

    #  /assetmanage/audio/1/
    url(r'^audio/(?P<pk>[0-9]+)/$', views.AudioDetailsView.as_view(), name="audio_details"),

    #  /assetmanage/audio/add/
    url(r'^audio/add/$', views.AudioCreate.as_view(), name="audio_add"),

    #  /assetmanage/audio/1/update/
    url(r'^audio/(?P<pk>[0-9]+)/update/$', views.AudioUpdate.as_view(), name="audio_update"),

    #  /assetmanage/audio/1/delete/
    url(r'^audio/(?P<pk>[0-9]+)/delete/$', views.AudioDelete.as_view(), name="audio_delete"),

    #  /assetmanage/subtitles/
    url(r'^subtitles/$', views.SubtitlesView.as_view(), name="subtitles"),

    #  /assetmanage/subtitle/1/
    url(r'^subtitle/(?P<pk>[0-9]+)/$', views.SubtitleDetailsView.as_view(), name="subtitle_details"),

    #  /assetmanage/subtitle/add/
    url(r'^subtitle/add/$', views.SubtitleCreate.as_view(), name="subtitle_add"),

    #  /assetmanage/subtitle/1/update/
    url(r'^subtitle/(?P<pk>[0-9]+)/update/$', views.SubtitleUpdate.as_view(), name="subtitle_update"),

    #  /assetmanage/subtitle/1/delete/
    url(r'^subtitle/(?P<pk>[0-9]+)/delete/$', views.SubtitleDelete.as_view(), name="subtitle_delete"),

]
