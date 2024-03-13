from django.urls import path

from . import views
app_name = "Homes"
urlpatterns = [
    path("", views.Home, name="Home"),
        path('contact-us/', views.Home, name='contact_us'),
    path('about-us/', views.Home, name='about_us'),
    path('blog/', views.Home, name='blog'),
]