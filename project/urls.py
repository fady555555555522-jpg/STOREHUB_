from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
#from .view import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/', include('pages.api_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#handler404 = handler404
#handler500 = handler500

