from django.urls import path
from . import views 
urlpatterns = [

    path("index.html", views.index),
    path("geziler", views.geziler),
    path("gezidetay/<slug:slug>", views.gezidetay)
]