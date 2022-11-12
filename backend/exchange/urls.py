from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gpw.urls')),
    path('celery-progress/', include('celery_progress.urls')),
]
