from django.shortcuts import render
from django.http import JsonResponse
import json

from django.views.decorators.csrf import ensure_csrf_cookie
from .models import *


# Create your views here.
@ensure_csrf_cookie
def index(request):
    products = Product.objects.all()

    cart_items = []
    cart_cookie = {}
    id_in_cart = []

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user)
        cart_items = order.cart_items.all()
    else:
        try:
            cart_cookie = json.loads(request.COOKIES["cart"])
            print(cart_cookie)
            id_in_cart = [int(key) for key in cart_cookie.keys()]
        except:
            cart_cookie = {}
            print("CART:", cart_cookie)

        order = {"get_cart_total": 0}

        for i in cart_cookie:
            try:
                if (
                    cart_cookie[i]["quantity"] > 0
                ):  # items with negative quantity = lot of freebies
                    product = Product.objects.get(id=i)
                    total = product.price * cart_cookie[i]["quantity"]

                    order["get_cart_total"] += total

                    cart_item = {
                        "product": {
                            "id": int(product.id),
                            "color": product.color,
                            "image": product.image,
                            "name": product.name,
                            "price": product.price,
                        },
                        "quantity": cart_cookie[i]["quantity"],
                        "get_total": round(total, 2),
                    }

                    cart_items.append(cart_item)

            except:
                pass

    order["get_cart_total"] = format(order["get_cart_total"], ".2f")

    context = {
        "products": products,
        "order": order,
        "items": cart_items,
        "id_in_cart": id_in_cart,
    }

    return render(request, "simpleCart/index.html", context)
