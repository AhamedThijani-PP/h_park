from django.contrib import admin
from . models import category,category_product,Slider

# Register your models here.
admin.site.register(category)
admin.site.register(category_product)
admin.site.register(Slider)