from django.conf.urls import url
from . import views


app_name = "projectmanage"


urlpatterns = [
    #  /projectmanage/
    url(r'^$', views.index, name="index"),

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

    #  /projectmanage/provider/1/delete/
    url(r'^provider/(?P<pk>[0-9]+)/delete/$', views.ProviderDelete.as_view(), name="provider_delete"),

    #  /projectmanage/project/1/delete/
    url(r'^project/(?P<pk>[0-9]+)/delete/$', views.ProjectDelete.as_view(), name="project_delete"),

]
