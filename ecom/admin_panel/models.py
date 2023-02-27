from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    img = models.ImageField(upload_to='/images')
