from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# def Contactus(request):
#     return HttpResponse("Contactus")

def Contactus(request):
    return render(request, "Contactus/contactus.html")