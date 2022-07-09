from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from coderedcms import admin_urls as coderedadmin_urls
from coderedcms import search_urls as coderedsearch_urls
from coderedcms import urls as codered_urls


urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('admin/', include(coderedadmin_urls)),
    path("", include(wagtail_urls)),
    path('documents/', include(wagtaildocs_urls)),
    #path('search/', include(coderedsearch_urls)),
    path('', include(codered_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
