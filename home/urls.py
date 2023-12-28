from django.urls import path
from . import views



urlpatterns = [
    path("all", views.allapp),
    path("Home", views.home),
    path("about", views.about),
    path("resume", views.resume),
    path("skill", views.skills),
    path("contact", views.contact),
    path("project", views.project),
]
