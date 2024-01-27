from django import forms

from shop.models import Product, Delivery, Category


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = [
            "type",
            "price",
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "name",
            "mass",
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "product_image",
            "description",
            "price",
            "availability",
            "category",
        ]
