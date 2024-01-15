from typing import Any
from django.db.models.query import QuerySet
from django.forms.forms import BaseForm
from django.http.response import HttpResponse
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

from shop.models import Shop, Product, Delivery, Category
from shop.forms import ProductForm, DeliveryForm, CategoryForm


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


class ShopListView(ListView):
    model = Shop
    template_name = "shop_list.html"


class ShopDetailView(LoginRequiredMixin, ListView):
    model = Shop
    template_name = "shop_detail.html"


"""
Delivery Views
"""


class DeliveryCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Delivery
    form_class = DeliveryForm
    template_name = "delivery_create.html"
    success_message = "Delivery Type created successfully"
    success_url = reverse_lazy("accounts:dashboard")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.shop = self.request.user.shop
        return super().form_valid(form)


"""
Category Views
"""


class CategoryCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "category_create.html"
    success_message = "Category created successfully"
    success_url = reverse_lazy("accounts:dashboard")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.shop = self.request.user.shop
        return super().form_valid(form)


"""
Product Views
"""


class ProductCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_create.html"
    success_message = "Product Type created successfully"
    success_url = reverse_lazy("accounts:dashboard")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.shop = self.request.user.shop
        return super().form_valid(form)


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "product_list.html"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product_detail.html"


class ProductUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "product_update.html"
    success_message = "Product Updated"
    fields = [
        "availability",
        "price",
    ]
    success_url = reverse_lazy("accounts:dashboard")

    def get_queryset(self) -> QuerySet[Any]:
        return Product.objects.filter(created_by=self.request.user)


"""
Allow vendors to create ads
Pay for advertisement space
Advertising Templates
"""
