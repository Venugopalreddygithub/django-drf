from django.db import models
from tags.models import Tags 
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True)
    tags = models.ManyToManyField(Tags, blank=True)
    image = models.URLField(max_length=2048, default='https://example.com/default-image.jpg')
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "products"
    