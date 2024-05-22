from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Posts(models.Model):
    problem = models.CharField(max_length=100)
    auto = models.TextField(max_length=1000)
    date = models.DateField(auto_now_add=False)
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

    def get_absolute_url(self):
        return f'/{self.pk}/'

class Postes(models.Model):
    problem = models.CharField(max_length=100)
    auto = models.TextField(max_length=1000)
    date = models.DateField(auto_now_add=False)
    author = models.CharField(max_length=1000)
    status = models.CharField(max_length=100)

    def get_absolute_url(self):
        return f'/{self.pk}/'