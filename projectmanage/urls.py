from django.conf.urls import url
from . import views


app_name = "projectmanage"


urlpatterns = [
    #  /projectmanage/
    url(r'^$', views.index, name="index"),

    #  /projectmanage/index_providers
    url(r'^index_providers$', views.index_providers, name="index_providers"),

    #  /projectmanage/index_rejections
    url(r'^index_rejections$', views.index_rejections, name="index_rejections"),

    #  /projectmanage/video/xml/download
    url(r'^project/(?P<pk>[0-9]+)/xml/video/download/$', views.download_video_xml, name="download_video_xml"),

    #  /projectmanage/audio/xml/download
    url(r'^project/(?P<pk>[0-9]+)/xml/audio/download/$', views.download_audio_xml, name="download_audio_xml"),

    #  /projectmanage/subtitle/xml/download
    url(r'^project/(?P<pk>[0-9]+)/xml/subtitle/download/$', views.download_subtitle_xml, name="download_subtitle_xml"),

    #  /projectmanage/providers/
    url(r'^providers/$', views.ProvidersView.as_view(), name="providers"),

    #  /projectmanage/projects/
    url(r'^projects/$', views.ProjectsView.as_view(), name="projects"),

    #  /projectmanage/search/
    url(r'^search/$', views.search, name="search"),

    #  /projectmanage/provider/1/
    url(r'^provider/(?P<pk>[0-9]+)/$', views.ProviderDetailsView.as_view(), name="provider_details"),

    #  /projectmanage/project/1/
    url(r'^project/(?P<pk>[0-9]+)/$', views.ProjectDetailsView.as_view(), name="project_details"),

    #  /projectmanage/provider/add/
    url(r'^provider/add/$', views.ProviderCreate.as_view(), name="provider_add"),

    #  /projectmanage/project/add/
    url(r'^project/add/$', views.ProjectCreate.as_view(), name="project_add"),

    #  /projectmanage/provider/1/update/
    url(r'^provider/(?P<pk>[0-9]+)/update/$', views.ProviderUpdate.as_view(), name="provider_update"),

    #  /projectmanage/project/1/update/
    url(r'^project/(?P<pk>[0-9]+)/update/$', views.ProjectUpdate.as_view(), name="project_update"),

    #  /projectmanage/project/1/operator/
    url(r'^project/(?P<pk>[0-9]+)/operator/$', views.ProjectOperator.as_view(), name="project_operator"),

    #  /projectmanage/project/1/status/
    url(r'^project/(?P<pk>[0-9]+)/status/$', views.ProjectStatus.as_view(), name="project_status"),

    #  /projectmanage/provider/1/delete/
    url(r'^provider/(?P<pk>[0-9]+)/delete/$', views.ProviderDelete.as_view(), name="provider_delete"),

    #  /projectmanage/project/1/delete/
    url(r'^project/(?P<pk>[0-9]+)/delete/$', views.ProjectDelete.as_view(), name="project_delete"),

    #  /projectmanage/rejections/
    url(r'^rejections/$', views.RejectionsView.as_view(), name="rejections"),

    #  /projectmanage/rejection/1/
    url(r'^rejection/(?P<pk>[0-9]+)/$', views.RejectionDetailsView.as_view(), name="rejection_details"),

    #  /projectmanage/rejection/add/
    url(r'^rejection/add/$', views.RejectionCreate.as_view(), name="rejection_add"),

    #  /projectmanage/rejection/1/update/
    url(r'^rejection/(?P<pk>[0-9]+)/update/$', views.RejectionUpdate.as_view(), name="rejection_update"),

    #  /projectmanage/rejection/1/delete/
    url(r'^rejection/(?P<pk>[0-9]+)/delete/$', views.RejectionDelete.as_view(), name="rejection_delete"),

]
