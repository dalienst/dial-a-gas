from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

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
    success_message = "Product created successfully"
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


"""
combined category and delivery
"""


# class DeliveryCategoryCreateView(LoginRequiredMixin, FormView):
#     template_name = "delivery_category_create.html"
#     success_url = reverse_lazy("accounts:dashboard")

#     def get(self, request, *args, **kwargs):
#         delivery_form = DeliveryForm()
#         category_form = CategoryForm()
#         return self.render_to_response(
#             self.get_context_data(
#                 delivery_form=delivery_form, category_form=category_form
#             )
#         )

#     def post(self, request, *args, **kwargs):
#         delivery_form = DeliveryForm(request.POST)
#         category_form = CategoryForm(request.POST)

#         if delivery_form.is_valid():
#             delivery = delivery_form.save(commit=False)
#             delivery.created_by = request.user
#             delivery.shop = request.user.shop
#             delivery.save()
#             return self.form_valid(delivery_form, category_form)

#         elif category_form.is_valid():
#             category = category_form.save(commit=False)
#             category.created_by = request.user
#             category.shop = request.user.shop
#             category.save()
#             return self.form_valid(delivery_form, category_form)

#         else:
#             return self.form_invalid(delivery_form, category_form)

#     def form_valid(self, delivery_form, category_form):
#         # Handle successful form submission
#         return super().form_valid(delivery_form, category_form)

#     def form_invalid(self, delivery_form, category_form):
#         # Handle form validation errors
#         return self.render_to_response(
#             self.get_context_data(
#                 delivery_form=delivery_form, category_form=category_form
#             )
#         )


# class DeliveryCategoryCreateView(FormView):
#     template_name = "delivery_category_create.html"
#     success_url = reverse_lazy("accounts:dashboard")

#     def get_form_class(self):
#         # Determine which form class to use based on the submitted data
#         if "delivery_form-submitted" in self.request.POST:
#             return DeliveryForm
#         elif "category_form-submitted" in self.request.POST:
#             return CategoryForm
#         else:
#             # Default to DeliveryForm if no specific form is submitted
#             return DeliveryForm

#     def get(self, request, *args, **kwargs):
#         # Use get_form_class to dynamically determine the form class
#         form_class = self.get_form_class()
#         form = form_class()
#         return self.render_to_response(self.get_context_data(form=form))

#     def post(self, request, *args, **kwargs):
#         # Use get_form_class to dynamically determine the form class
#         form_class = self.get_form_class()
#         form = form_class(request.POST)

#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.created_by = request.user
#             instance.shop = request.user.shop
#             instance.save()
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

#     def form_valid(self, form):
#         # Handle successful form submission
#         return super().form_valid(form)

#     def form_invalid(self, form):
#         # Handle form validation errors
#         return self.render_to_response(self.get_context_data(form=form))
