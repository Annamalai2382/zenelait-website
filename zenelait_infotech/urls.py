from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('zenelait_infotech.api_urls')), # For future separation or DRF consumers
    path('', include('core.urls')),
    path('services/', include('services.urls')),
    path('blog/', include('blog.urls')),
    path('careers/', include('careers.urls')),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
