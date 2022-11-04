from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("index")

def geziler(request):
    return HttpResponse("geziler")

def gezidetay(request , slug):
    return HttpResponse("gezidetay: " + slug)
