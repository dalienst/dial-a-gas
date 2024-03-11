from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from shop.models import Shop, Product, Order
from shop.forms import ProductForm, OrderForm
from shop.utils import send_sms


class ShopUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Shop
    template_name = "shop_update.html"
    success_message = "Shop Information Updated Successfully"
    fields = [
        "image",
        "name",
        "location",
        "shop_contact",
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
Product Views
"""


class ProductCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_create.html"
    success_message = "Product created successfully"
    success_url = reverse_lazy("accounts:dashboard")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.shop = self.request.user.shop
        form.instance.shop_contact = self.request.user.shop.contact
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
        "name",
        "product_image",
        "availability",
        "price",
        "mass",
    ]
    success_url = reverse_lazy("accounts:dashboard")

    def get_queryset(self) -> QuerySet[Any]:
        return Product.objects.filter(created_by=self.request.user)


class ProductDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "product_delete.html"
    success_message = "Product Deleted Successfully"
    success_url = reverse_lazy("accounts:dashboard")


"""
Order Views
"""


class OrderCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = "order_create.html"
    success_message = "Order created successfully"
    success_url = reverse_lazy("accounts:dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs.get("pk")
        product = get_object_or_404(Product, id=product_id)
        context["product"] = product
        return context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.product = self.get_context_data()["product"]
        product_name = form.instance.product.name
        response = super().form_valid(form)

        # Sending sms
        order = form.instance
        order_reference = order.id
        vendor_shop_contact = order.shop_contact
        client = order.created_by.username
        client_contact = order.contact
        client_location = order.location

        # Constructing a more professional message
        message = (
            f"New Order Received:\n"
            f"Order Reference: {order_reference}\n"
            f"Customer: {client}\n"
            f"Contact: {client_contact}\n"
            f"Delivery Location: {client_location}\n"
            f"Product: {product_name}\n"
            f"Please coordinate with the customer for delivery."
        )

        send_sms(to=vendor_shop_contact, body=message)

        return response
