from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('cars.urls')),
    path('', include('parser_app.urls')),
    path('', include('custom_users.urls')),
    path('', include('product.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
