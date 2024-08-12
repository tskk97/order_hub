from django.contrib import admin
from catalogue.models import Category, Product
from orders.models import Order, OrderItem

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
