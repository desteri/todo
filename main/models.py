from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class BookShop(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=150)
    year = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
