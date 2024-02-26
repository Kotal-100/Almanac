from django.shortcuts import render
from django.http import HttpResponse
#from django.http import HttpResponse



# def Aboutus(request):
#     return HttpResponse("Aboutus")


def Aboutus(request):
    return render(request, "Aboutus/aboutus.html")