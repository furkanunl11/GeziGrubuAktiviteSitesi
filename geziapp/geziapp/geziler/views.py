from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def geziler(request):
    return render(request, 'geziler.html')

def gezidetay(request , slug):
    return render(request, 'gezidetay.html', {
        slug: slug
    })