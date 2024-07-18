from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_data', null=True)
    name = models.CharField(max_length=100, null=True)
    UUID = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    def get_total_count(self):
        return self.item_set.count()


class Item(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class List(models.Model):
    name = models.CharField(max_length=100, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

