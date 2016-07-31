from django.conf.urls import url
from . import views


app_name = "administration"


urlpatterns = [

    #  /administration/
    url(r'^$', views.index, name="index"),

    #  /administration/database/
    url(r'^database/$', views.database, name="database"),

    #  /administration/project_database_image/
    url(r'^database/project_database_image/$', views.project_database_image, name="project_database_image"),

    #  /administration/global_database_image/
    url(r'^database/global_database_image/$', views.global_database_image, name="global_database_image"),

]
