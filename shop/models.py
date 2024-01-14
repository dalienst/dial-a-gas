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
    image = CloudinaryField("shop_images", blank=True, null=True)
    contact = models.BigIntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
