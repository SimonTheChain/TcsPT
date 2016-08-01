from django.conf.urls import url
from . import views


app_name = "assetmanage"


urlpatterns = [

    #  /assetmanage/
    url(r'^$', views.index, name="index"),

    #  /assetmanage/assets/
    url(r'^assets/$', views.AssetsView.as_view(), name="assets"),

    #  /assetmanage/videos/
    url(r'^videos/$', views.VideosView.as_view(), name="videos"),

    #  /assetmanage/search/
    url(r'^search/$', views.search, name="search"),

    #  /assetmanage/asset/1/
    url(r'^asset/(?P<pk>[0-9]+)/$', views.AssetDetailsView.as_view(), name="asset_details"),

    #  /assetmanage/asset/select/
    url(r'^asset/select/$', views.asset_select, name="asset_select"),

    #  /assetmanage/video/add/
    #  url(r'^video/add/$', views.add_video, name="video_add"),
    url(r'^video/add/$', views.CreateVideoAsset.as_view(), name="video_add"),

    #  /assetmanage/assets/
    url(r'^videos/$', views.AssetsView.as_view(), name="assets"),

    #  /assetmanage/asset/add/
    url(r'^asset/add/$', views.AssetCreate.as_view(), name="asset_add"),

    #  /assetmanage/asset/1/update/
    url(r'^asset/(?P<pk>[0-9]+)/update/$', views.AssetUpdate.as_view(), name="asset_update"),

    #  /assetmanage/asset/1/delete/
    url(r'^asset/(?P<pk>[0-9]+)/delete/$', views.AssetDelete.as_view(), name="asset_delete"),

]
