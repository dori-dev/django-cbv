"""config URL Configuration
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('', include('app.urls')),
    # path('', include('django.contrib.auth.urls')),
]
