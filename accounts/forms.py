from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Client, Vendor, Admin
from django.db import transaction
from django.contrib.auth import get_user_model
from shop.models import Shop

User = get_user_model()


class ClientCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        Client.objects.create(user=user)
        return user


class VendorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_vendor = True
        user.save()
        Vendor.objects.create(user=user)
        Shop.objects.create(owner=user)
        return user


class AdminCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        Admin.objects.create(user=user)
        return user
