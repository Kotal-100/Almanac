from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import Blog
# Create your views here.



def blog(request):
   displays= Blog.objects.get(id=1)
   template = "Blog/Blog.html"
   context = {
               
      'display':displays,
    }
   return render(request, template ,context)
    