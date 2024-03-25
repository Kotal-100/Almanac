from django.shortcuts import render,redirect
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from .models import Contactus
# Create your views here.



# def Contactus(request):
#     return HttpResponse("Contactus")

def contactus(request):
    if request.method == "GET":
        return render(request, "Contactus/contactus.html")
    
    elif request.method == "POST":
        name =request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        user= Contactus(name=name,email=email,message=message)
        user.save()
        return redirect("/contact-us/",message="message")

# # def Contactus(request):
#   name =request.POST.get("name")
#   email = request.POST.get("email")
#   message = request.POST.get("message")
#   return HttpResponse( "Message successfully sent",name,email,message)

# def contactus(request):
#    displays= contactus.objects.get(name,email,message)
#    template = "Contactus/Contactus.html"
#    context = {
               
#       'display':displays,
#     }
#    return JsonResponse(request, template ,context)