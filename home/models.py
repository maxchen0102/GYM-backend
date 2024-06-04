from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=100, null=True)
