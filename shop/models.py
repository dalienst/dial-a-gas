from django.db import models
from django.contrib.auth import get_user_model

from accounts.abstracts import UniversalIdModel, TimeStampedModel
from cloudinary.models import CloudinaryField


User = get_user_model()


class Shop(UniversalIdModel, TimeStampedModel):
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=1000, blank=True, null=True)
    location = models.CharField(max_length=1000, blank=True, null=True)
    image = CloudinaryField("Shop Image", blank=True, null=True)
    contact = models.BigIntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Delivery(models.Model):
    TYPE_CHOICES = [
        ("selfpickup", "Pickup Gas by yourself"),
        ("delivery", "Get your gas delivered at your doorstep"),
    ]

    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    price = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="deliveries")

    class Meta:
        verbose_name_plural = "Deliveries"

    def __str__(self) -> str:
        return self.type


class Category(models.Model):
    MASS_CHOICES = [
        ("6kg", "Small - 6kg"),
        ("13kg", "Medium - 13kg"),
        ("26kg", "Large - 26kg"),
        # Add other choices as needed
    ]

    name = models.CharField(max_length=100)
    mass = models.CharField(max_length=100, choices=MASS_CHOICES, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="categories")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"{self.name} - {self.mass}"


class Product(UniversalIdModel, TimeStampedModel):
    name = models.CharField(max_length=1000)
    product_image = CloudinaryField("Product Image", blank=True, null=True)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True
    )
    price = models.PositiveIntegerField()
    availability = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="products")

    class Meta:
        indexes = [
            models.Index(fields=["name", "price", "availability"]),
        ]

    def __str__(self) -> str:
        return self.name
