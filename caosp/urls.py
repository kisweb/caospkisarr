from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include
from api.urls import app

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include('account.urls')),
    path("", include('core.urls')),
    path("etablissements/", include('etablissement.urls')),
    path("gestion/", include('gestion.urls')),
    path("quotes/", include('quote.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path("commandes/", include("commande.urls")),
    path("api/kisarrweb/", app.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()