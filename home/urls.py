from django.urls import path
from . import views



urlpatterns = [
    path("Home", views.home),
    path("about", views.about),
    path("resume", views.resume),
    path("skills", views.skills),
    path("contact", views.contact),
]
