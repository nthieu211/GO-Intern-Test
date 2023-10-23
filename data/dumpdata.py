import json

# References: https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata
if __name__ == "__main__":
    file_path = "data\shoes.json"

    product_list = []

    with open(file_path, "r") as f:
        data = json.load(f)
        data = data["shoes"]
        for product in data:
            pk = product["id"]
            product.pop("id", None)

            product = {
                "pk": pk,
                "model": "simpleCart.Product",
                "fields": product,
            }
            product_list.append(product)
        f.close()

    with open("product.json", "w") as f:
        json.dump(product_list, f, indent=4)
        f.close()
