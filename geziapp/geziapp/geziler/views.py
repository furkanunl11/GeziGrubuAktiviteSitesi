from django.shortcuts import render
from datetime import date

data = {
    "geziler": [
        {
            "title":"gezi1",
            "description": "gezi aciklama1",
            "imageUrl": "venedik.jpg",
            "slug": "gezi-adi-1",
            "language":"english",
            "date": date(2021,5,10)
        },
        {
            "title":"gezi2",
            "description": "gezi aciklama2",
            "imageUrl": "arjantin.jpg",
            "slug": "gezi-adi-2",
            "language":"english",
            "date": date(2021,10,5)
        },
        {
            "title":"gezi3",
            "description": "gezi aciklam31",
            "imageUrl": "filipinler.jpg",
            "slug": "gezi-adi-3",
            "language":"english",
            "date": date(2021,10,10)
        },
        {
            "title":"gezi4",
            "description": "gezi aciklama4",
            "imageUrl": "irlanda.jpg",
            "slug": "gezi-adi-4",
            "language":"english",
            "date": date(2021,3,10)
        },
        {
            "title":"gezi5",
            "description": "gezi aciklama5",
            "imageUrl": "ispanya.jpg",
            "slug": "gezi-adi-4",
            "language":"english",
            "date": date(2021,3,10)
        },
        {
            "title":"gezi6",
            "description": "gezi aciklama6",
            "imageUrl": "japonya2.png",
            "slug": "gezi-adi-6",
            "language":"english",
            "date": date(2021,3,10)
        },
        {
            "title":"gezi7",
            "description": "gezi aciklama7",
            "imageUrl": "norvec2.jpg",
            "slug": "gezi-adi-7",
            "language":"english",
            "date": date(2021,3,10)
        },
        {
            "title":"gezi8",
            "description": "gezi aciklama8",
            "imageUrl": "turkiye.jpg",
            "slug": "gezi-adi-8",
            "language":"english",
            "date": date(2021,3,10)
        },
        {
            "title":"gezi9",
            "description": "gezi aciklama9",
            "imageUrl": "venedik2.jpg",
            "slug": "gezi-adi-9",
            "language":"english",
            "date": date(2021,3,10)
        }
    ],
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
    geziler = data["geziler"][-4:]
    sliders = data["sliders"]
    return render(request, 'index.html', {
        "geziler": geziler,
        "sliders": sliders
    })

def geziler(request):
    geziler = data["geziler"]
    return render(request, 'geziler.html' , {
        "geziler": geziler
    })

def gezidetay(request , slug):
    geziler = data["geziler"]

    """secilenGezi = None
    for gezi in geziler:
        if gezi["slug"] == slug:
            secilenGezi = gezi"""

    secilenGezi = next(gezi for gezi in geziler if gezi["slug"] == slug)

    return render(request, 'gezidetay.html', {
        "gezi": secilenGezi
    })