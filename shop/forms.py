from django import forms

from shop.models import Product,  Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "product_image",
            "price",
            "availability",
            "mass",
        ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "contact",
            "location",
        ]
