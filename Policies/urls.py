from django.urls import path

from . import views

urlpatterns = [
    path("", views.Policies, name="Policies"),
]