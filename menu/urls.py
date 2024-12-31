from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="home"),
    path('Category', views.Category,name="Category"),
    path('contact', views.contact,name="contact"),
    path('about', views.about,name="about"),
    path('Category/<str:slug>',views.Category_product,name="category_product"),
]
