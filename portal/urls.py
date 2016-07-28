from django.conf.urls import url
from . import views


app_name = "portal"


urlpatterns = [

    #  /portal/
    url(r'^$', views.index, name="index"),

    # login/logout
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),

    #  /portal/login/
    # url(r'^login/$', views.UserFormView.as_view(), name="login"),

    # url(r'^login/$', 'django.contrib.auth.views.login', {
    #     'template_name': 'portal/login.html'
    # }),

]
