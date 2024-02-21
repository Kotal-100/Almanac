from django.urls import path

from . import views
app_name = "Home"
urlpatterns = [
    path("", views.Home, name="Home"),
     path("contact-us/", views.Home, name="contact_us"),
]