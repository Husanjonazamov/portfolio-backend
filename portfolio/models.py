from django.db import models
from django.utils.text import slugify



class Category(models.Model):
    name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name


class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    category = models.ForeignKey(Category, related_name='portfolios', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/')
    githup = models.CharField(max_length=150)
    projects = models.CharField(max_length=155)
    
    def __str__(self):
        return self.title

