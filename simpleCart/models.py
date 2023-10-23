from django.db import models
from django.contrib.auth.models import User, AnonymousUser
import uuid  # Auto generate ID

# Create your models here.


class ServerUser(AnonymousUser):
    @property
    def is_authenticated(self):
        return True


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.URLField(max_length=200, null=True)
    color = models.CharField(max_length=7, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    transaction_id = models.UUIDField(
        max_length=100, unique=True, default=uuid.uuid4, primary_key=True
    )
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.transaction_id)

    @property
    def get_cart_total(self):
        order_items = self.cart_items.all()
        total = sum([item.get_total for item in order_items])
        return total


class CartItems(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product"
    )
    cart = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name

    @property
    def get_total(self):
        return self.product.price * self.quantity
