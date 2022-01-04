from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
from django.urls import reverse
# Create your models here.

class User(AbstractUser):
 pass

class Plan(models.Model):
 name = models.CharField(max_length=64)
 description = models.CharField(max_length=256)

class Fragment(models.Model):
 date = models.DateField()
 calories = models.IntegerField()
 burnt = models.IntegerField()
 carbs = models.IntegerField()
 fats = models.IntegerField()
 proteins = models.IntegerField()

class Profile(models.Model):
 user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
 age = models.IntegerField()
 days = models.ManyToManyField(Fragment)
 plan = models.OneToOneField(Plan, on_delete=models.CASCADE, null=True, blank=True)

