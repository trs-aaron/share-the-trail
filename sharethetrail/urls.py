from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from coderedcms import admin_urls as coderedadmin_urls
from coderedcms import urls as codered_urls
from health_check import urls as healthcheck_urls
from sharethetrail.views import error_400, error_403, error_404, error_500


handler400 = error_400
handler403 = error_403
handler404 = error_404
handler500 = error_500

urlpatterns = [
    path('sitemap.xml', sitemap),
    path('health/', include(healthcheck_urls)),
    path('django-admin/', admin.site.urls),
    path('admin/', include(coderedadmin_urls)),
    path("", include(wagtail_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('', include(codered_urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
