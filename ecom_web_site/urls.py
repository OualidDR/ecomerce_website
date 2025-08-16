

from django.contrib import admin
from django.urls import path
from store.views import home_view, about_view, logout_view, login_view, register_view
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin', admin.site.urls),
    path('home', home_view, name="home"),
    path('about', about_view, name="about"),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('register', register_view, name="register")

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


