from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, default=None)
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    tags = models.ManyToManyField('Tag', related_name='products')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
