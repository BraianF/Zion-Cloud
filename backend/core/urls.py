"""core URL Configuration
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/customers/', include('customers.urls')),
    path('api/servers/', include('servers.urls')),
    path('api/backups/', include('backups.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    # Djago browser reload
    urlpatterns.append(path("__reload__/", include("django_browser_reload.urls"))) # type: ignore
    # Debug toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls))) # type: ignore