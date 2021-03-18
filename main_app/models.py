from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=10000)
    creation_date = models.DateField()
    image_url = models.CharField(max_length=150)
    rating = models.IntegerField()
    brand = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    url = models.SlugField(max_length=50)
    
    def __str__(self):
        return self.product_name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    creation_date = models.DateField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_age = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    photo = ImageField(blank=True, manual_crop="")


