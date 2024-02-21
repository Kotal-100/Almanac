from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



# def Home(request):
#     return HttpResponse("Home")

def Home(request):
    return render(request, "home/index.html")
  