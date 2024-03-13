from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import AboutUs
#from django.http import HttpResponse



# def Aboutus(request):
#     return HttpResponse("Aboutus")


# def Aboutus(request):
#     return render(request, "Aboutus/aboutus.html")

def Aboutus(request):
    displays = AboutUs.objects.get(id=1)
    template = "Aboutus/aboutus.html"
    context = {
               
      'display':displays,
    }
    return render(request, template ,context)
    
   