from django.db import models

# Create your models here.
class Meetups(models.Model):
    title= models.CharField(max_length=200)
    slug= models.SlugField(unique=True)
    description= models.TextField()
    image = models.ImageField()