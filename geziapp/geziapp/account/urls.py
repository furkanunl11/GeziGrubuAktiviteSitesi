from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('login',views.login_request, name = "login"),
    path('register',views.register_request, name = "register"),
    path('change_password',views.change_password, name = "change_password"),
    path('logout',views.logout_request, name = "logout"),
    path('change-password',views.change_password, name="change_password"),
    path('profile',views.profile, name="profile"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
