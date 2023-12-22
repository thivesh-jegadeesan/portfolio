from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("portfolio/", include('home.urls')),
    path("admin/", admin.site.urls),
]
