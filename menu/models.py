from django.db import models

# Create your models here.
class category(models.Model):
    slug=models.CharField(max_length=50,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)
    image=models.ImageField(upload_to='imagess',null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    def __str__(self):
        return self.name
    
class category_product(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=False,blank=False)
    product_image=models.ImageField(upload_to='imagess',null=False,blank=False)
    price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    def __str__(self):
        return self.name

class Slider(models.Model):
    slider_image=models.ImageField(upload_to='imagess',null=False,blank=False)
    title=models.CharField(max_length=50,null=False,blank=False)
    description=models.CharField(max_length=100,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    def __str__(self):
        return self.title