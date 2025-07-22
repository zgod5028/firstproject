from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # ваш основной app
    path('accounts/', include('django.contrib.auth.urls')),
    path('app/', include('app.urls')),
    # встроенные маршруты: login, logout
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)