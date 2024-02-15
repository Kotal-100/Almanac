from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def Dashboard(request):
    return HttpResponse("dashboard")


def user(request):
    return HttpResponse("user")


def institution(request):
    return HttpResponse("institution")


def roles(request):
    return HttpResponse("roles")