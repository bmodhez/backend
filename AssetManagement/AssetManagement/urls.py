from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from assets.views.asset_views import assigned   # 👈 FIX HERE

urlpatterns = [
    path("admin/", admin.site.urls),
    path("test/", assigned, name="test"),
    path("api/users/", include("users.urls")),
    path("api/", include("assets.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
