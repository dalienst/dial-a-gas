from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver

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
    shop_contact = models.CharField(
        blank=True,
        null=True,
        max_length=9,
        help_text=_(
            "Enter the shop contact number without the country code e.g: 712345678."
        ),
    )
    contact = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


@receiver(pre_save, sender=Shop)
def format_shop_contact(sender, instance, **kwargs):
    # Format the contact number with the country code before saving
    if instance.shop_contact:
        instance.contact = f"+254{instance.shop_contact}"


class Product(UniversalIdModel, TimeStampedModel):
    name = models.CharField(max_length=1000)
    product_image = CloudinaryField("Product Image", blank=True, null=True)
    MASS_CHOICES = [
        ("6kg", "Small - 6kg"),
        ("13kg", "Medium - 13kg"),
        ("26kg", "Large - 26kg"),
        # Add other choices as needed
    ]
    mass = models.CharField(max_length=100, choices=MASS_CHOICES)
    price = models.PositiveIntegerField()
    availability = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="products")
    shop_contact = models.CharField(max_length=20)

    class Meta:
        indexes = [
            models.Index(fields=["name", "price", "availability"]),
        ]

    def __str__(self) -> str:
        return self.name


class Order(UniversalIdModel, TimeStampedModel):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="orders_related_to_product"
    )
    shop_contact = models.CharField(max_length=20)
    contact = models.CharField(
        max_length=20,
        help_text=_(
            "Enter the contact number with the country code e.g: +254712345678."
        ),
    )
    location = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = "Orders"

    def __str__(self) -> str:
        return f"{self.created_by.username} - {self.contact}"


@receiver(pre_save, sender=Order)
def update_shop_contact(sender, instance, **kwargs):
    # Ensure the product field is set before accessing its associated shop contact
    if not instance.shop_contact:
        instance.shop_contact = instance.product.shop_contact
