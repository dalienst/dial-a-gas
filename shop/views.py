from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from shop.models import Shop


class ShopUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Shop
    template_name = "shop_update.html"
    success_message = "Shop Information Updated Successfully"
    fields = [
        "image",
        "name",
        "location",
        "contact",
    ]
    success_url = reverse_lazy("accounts:dashboard")

    def get_queryset(self) -> QuerySet[Any]:
        return Shop.objects.filter(owner=self.request.user)
