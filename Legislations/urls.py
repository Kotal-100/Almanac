from django.urls import path
from . import views



urlpatterns = [
    path("", views.Legislations, name="Legislations"),
]