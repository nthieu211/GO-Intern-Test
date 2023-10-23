from django.contrib import admin
from .models import Product, Order, CartItems

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(CartItems)
