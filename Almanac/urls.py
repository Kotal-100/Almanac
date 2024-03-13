"""
URL configuration for Almanac project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from Contactus import views
from Dashboard import views as Dashboardviews

dashboard_urlpatterns = [
    path('user/', Dashboardviews.user, name='user'),
    path('institution/', Dashboardviews.institution, name='institution'),
    path('roles/', Dashboardviews.roles, name='roles'),
    
]



urlpatterns = [
    path("about-us/", include("Aboutus.urls")),
    path("blog/", include("Blog.urls")),
    path("community-engagement/", include("Communityengagement.urls")),
    path('contact-us/', views.Contactus, name='contact_us'),
    path("dashboard/", include(dashboard_urlpatterns)),
    path("", include("Home.urls")),
    path("legislations/", include("Legislations.urls")),
    path("policies/", include("Policies.urls")),
   
    path('admin/', admin.site.urls),
]
