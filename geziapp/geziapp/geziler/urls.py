from django.urls import path
from . import views 
urlpatterns = [

    path("anasayfa", views.index, name="home_page"),
    path("geziler", views.geziler, name="geziler_page"),
    path("gezidetay/<slug:slug>", views.gezidetay, name="gezi-detay"),
    path("hakkimizda",views.hakkimizda, name = "hakkimizda")
]