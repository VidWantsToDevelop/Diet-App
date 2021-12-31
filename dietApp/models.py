from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.

class User(AbstractUser):
 pass

class Fragment(models.Model):
 date = models.DateField(auto_now_add=True)
 calories = models.IntegerField()
 burnt = models.IntegerField()
 carbs = models.IntegerField()
 fats = models.IntegerField()
 proteins = models.IntegerField()

class Profile(models.Model):
 user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
 age = models.IntegerField()
 days = models.ManyToManyField(Fragment)

