from django.urls import path
from .views import homeview, about

urlpatterns = [
    path("", homeview, name="homepage"),
    path("about", about, name="about"),
]