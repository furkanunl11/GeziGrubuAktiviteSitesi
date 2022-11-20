from django.shortcuts import render, get_object_or_404
from datetime import date
from geziler.models import Category

data = {
    
        "sliders": [
            {
                "slider_image":"slider.jpg",
                "url":"gezi-adi-1"
            },
             {
                "slider_image":"slider1.jpg",
                "url":"gezi-adi-2"
            },
             {
                "slider_image":"slider2.png",
                "url":"gezi-adi-3"
            },
             {
                "slider_image":"slider3.jpg",
                "url":"gezi-adi-4"
            },
             {
                "slider_image":"slider4.jpg",
                "url":"gezi-adi-5"
            }
        ]

    
}

def index(request):
    geziler = Category.objects.filter(isActive = True,isHome = True)
    sliders = data["sliders"]
    return render(request, 'index.html', {
        "geziler": geziler,
        "sliders": sliders
    })

def geziler(request):
    geziler = Category.objects.filter(isActive = True)
    return render(request, 'geziler.html' , {
        "geziler": geziler
    })

def gezidetay(request , slug):
    gezi = get_object_or_404(Category, slug = slug)

    return render(request, 'gezidetay.html', {
        "gezi": gezi
    })