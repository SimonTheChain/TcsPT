from django.conf.urls import url
from . import views


app_name = "assetmanage"


urlpatterns = [

    #  /assetmanage/
    url(r'^$', views.index, name="index"),

    #  /assetmanage/assets/
    url(r'^assets/$', views.AssetsView.as_view(), name="assets"),

    #  /assetmanage/search/
    url(r'^search/$', views.search, name="search"),

    #  /assetmanage/asset/1/
    url(r'^asset/(?P<pk>[0-9]+)/$', views.AssetDetailsView.as_view(), name="asset_details"),

    #  /assetmanage/asset/select/
    url(r'^asset/select/$', views.asset_select, name="asset_select"),

    #  /assetmanage/asset/create/
    url(r'^asset/create/$', views.asset_create, name="asset_create"),

    #  /assetmanage/asset/test/
    url(r'^asset/test/$', views.asset_test, name="asset_test"),

    #  /assetmanage/asset/add/
    url(r'^asset/add/$', views.AssetCreate.as_view(), name="asset_add"),

    #  /assetmanage/asset/1/update/
    url(r'^asset/(?P<pk>[0-9]+)/update/$', views.AssetUpdate.as_view(), name="asset_update"),

    #  /assetmanage/asset/1/delete/
    url(r'^asset/(?P<pk>[0-9]+)/delete/$', views.AssetDelete.as_view(), name="asset_delete"),

]
