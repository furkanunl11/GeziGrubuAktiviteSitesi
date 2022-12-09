from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path("anasayfa", views.index, name="home_page"),
    path("geziler", views.geziler, name="geziler_page"),
    path("gezidetay/<slug:slug>", views.gezidetay, name="gezi-detay"),
    path("hakkimizda",views.hakkimizda, name = "hakkimizda"),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
