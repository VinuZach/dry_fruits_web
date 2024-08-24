from django.urls import path
from .views import *
urlpatterns = [
    path('', home_page,name="home"),
    path('products', products_page,name="products"),
    path('about_us', about_us,name="about_us"),
]