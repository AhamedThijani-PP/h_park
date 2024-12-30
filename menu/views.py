from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import category,category_product,Slider
from django.contrib import messages

# Create your views here.
def index(request):
    slider=Slider.objects.filter(status=0)
    return render(request,'index.html',{'slider':slider})

def Category(request):
    categories=category.objects.filter(status=0)
    return render(request,'category.html',context={'category':categories})

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def Category_product(request,slug):
    if (category.objects.filter(slug=slug,status=0)):
        menu_view=category_product.objects.filter(category__slug=slug)
    else:
        messages.error(request,"No Such Category")
        return redirect('Category')
    return render(request,'category_product.html',{'menu_view':menu_view})