from django.urls import path
from store.views import home_view, about_view, logout_view, login_view, register_view, product_view, category_view

urlpatterns = [
    
    path('', home_view, name="home"),
    path('about', about_view, name="about"),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('register', register_view, name="register"),
    path('category/<str:foo>', category_view, name="category"),
    path('product/<int:pk>', product_view, name="product")

] 
