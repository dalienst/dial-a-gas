from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.abstracts import UniversalIdModel, TimeStampedModel
from cloudinary.models import CloudinaryField
from gasdelivery.settings.base import AUTH_USER_MODEL


class User(AbstractUser, UniversalIdModel, TimeStampedModel):
    is_client = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def get_full_name(self) -> str:
        return super().get_full_name()

    def get_short_name(self) -> str:
        return super().get_short_name()

    def get_username(self) -> str:
        return super().get_username()


# @receiver(post_save, sender=User)
# def create_vendor_and_shop(sender, instance, created, **kwargs):
#     if created and instance.is_vendor:
#         vendor = Vendor.objects.create(user=instance)
#         Shop.objects.create(
#             owner=instance,
#             name=f"{instance.username}'s Shop",
#             location="Default Location",
#         )


class Client(TimeStampedModel):
    user = models.OneToOneField(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="client",
    )
    image = CloudinaryField("Client Image", blank=True, null=True)
    phone_number = models.BigIntegerField(blank=True, null=True)
    location = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username


class Vendor(TimeStampedModel):
    user = models.OneToOneField(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="vendor",
    )
    image = CloudinaryField("Vendor Images", blank=True, null=True)
    phone_number = models.BigIntegerField(blank=True, null=True)
    shop_location = models.CharField(max_length=1000, blank=True, null=True)


class Admin(TimeStampedModel):
    user = models.OneToOneField(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="admin",
    )
    image = CloudinaryField("admin_image", blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username
