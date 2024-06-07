from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    UUID = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

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

