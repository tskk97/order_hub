from django.db import models
from django.utils import timezone
from catalogue.models import Product


class Order(models.Model):
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order {self.id} at {self.date}"

    @property
    def total_price(self):
        total = sum(item.quantity *
                    item.product.price for item in self.items.all())
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
