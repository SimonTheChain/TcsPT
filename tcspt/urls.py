from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^portal/', include("portal.urls", namespace="portal")),
    url(r'^assetmanage/', include("assetmanage.urls", namespace="assetmanage")),
    url(r'^projectmanage/', include("projectmanage.urls", namespace="projectmanage")),
    url(r'^administration/', include("administration.urls", namespace="administration")),
    url(r'news/', include("news.urls", namespace="news")),
    url(r'metadata/', include("metadata.urls", namespace="metadata")),
    url(r'^search/', include("haystack.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
