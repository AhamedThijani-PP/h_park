from django.db import models
import os

# Create your models here.
class category(models.Model):
    slug=models.CharField(max_length=50,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)
    image=models.ImageField(upload_to='images/',null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    def __str__(self):
        return self.name
    def delete(self, *args, **kwargs):
        # Delete the image file from the file system before deleting the record
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)
    
class category_product(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=False,blank=False)
    product_image=models.ImageField(upload_to='images/',null=False,blank=False)
    price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    def __str__(self):
        return self.name
    def delete(self, *args, **kwargs):
        # Delete the product image from the file system before deleting the record
        if self.product_image:
            if os.path.isfile(self.product_image.path):
                os.remove(self.product_image.path)
        super().delete(*args, **kwargs)

class Slider(models.Model):
    slider_image=models.ImageField(upload_to='images/',null=False,blank=False)
    title=models.CharField(max_length=50,null=False,blank=False)
    description=models.CharField(max_length=100,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    def __str__(self):
        return self.title
    def delete(self, *args, **kwargs):
        # Delete the image file from the file system before deleting the record
        if self.slider_image:
            if os.path.isfile(self.slider_image.path):
                os.remove(self.slider_image.path)
        super().delete(*args, **kwargs)