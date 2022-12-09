from django.shortcuts import render, get_object_or_404
from datetime import date
from geziler.models import Category,Video,Comment,Slider
from geziler.forms import CommentForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse

from geziler.models import Category


def index(request):
    geziler = Category.objects.filter(isActive = True,isHome = True)
    sliders = Slider.objects.filter(is_active = True)
    return render(request, 'geziler/index.html', {
        "geziler": geziler,
        "sliders": sliders
    })

def geziler(request):
    geziler = Category.objects.filter(isActive = True)
    return render(request, 'geziler/geziler.html' , {
        "geziler": geziler
    })

def gezidetay(request , slug):
    gezi = get_object_or_404(Category, slug = slug)
    comment_form = CommentForm()

    if request.method == "POST": ### databaseye kayıt ekleme işlemi
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.gezi = gezi
            comment.save()
            return HttpResponseRedirect(reverse("gezi-detay",args=[slug] ))

    
    
    
    return render(request, 'geziler/gezidetay.html', {
        "gezi": gezi,
        "videos": gezi.video_set.all(),
        "comments": gezi.comments.all().order_by("-date_added"),
        "comment_form": comment_form
    })




def hakkimizda(request):
    return render(request, 'geziler/hakkimizda.html')
    