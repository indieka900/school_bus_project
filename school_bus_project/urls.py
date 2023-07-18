from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # User management
    path("accounts/", include("allauth.urls")),
    # local apps
    path('', include('school_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
