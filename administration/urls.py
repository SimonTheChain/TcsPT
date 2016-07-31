from django.conf.urls import url
from . import views


app_name = "administration"


urlpatterns = [

    #  /administration/
    url(r'^$', views.index, name="index"),

    #  /administration/database/
    url(r'^database/$', views.database, name="database"),

    #  /administration/database_image/
    url(r'^database/image/$', views.database_image, name="database_image"),

]
