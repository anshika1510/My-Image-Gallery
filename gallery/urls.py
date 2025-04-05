from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='index'),  # Homepage - image gallery
    path('slideshow/', views.slideshow_view, name='slideshow'),
    path('home/', views.home, name='home'),
    path('homepage/', views.homepage, name='homepage'),
]


