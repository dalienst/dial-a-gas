from django.shortcuts import render, redirect
from django.views.generic import TemplateView
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

from accounts.models import Admin, Client, Vendor
from accounts.forms import ClientCreationForm, VendorCreationForm, AdminCreationForm
from shop.models import Shop, Category, Product

User = get_user_model()


def landing(request):
    return render(request, "landing.html")


@login_required
def dashboard(request):
    client_profile = Client.objects.filter(user=request.user)
    vendor_profile = Vendor.objects.filter(user=request.user)
    vendor_shop = Shop.objects.filter(owner=request.user)
    vendor_category = Category.objects.filter(created_by=request.user)
    vendor_product = Product.objects.filter(created_by=request.user)
    client_products = Product.objects.filter(availability=True)
    return render(
        request,
        "accounts/dashboard.html",
        {
            "client_profile": client_profile,
            "vendor_profile": vendor_profile,
            "vendor_shop": vendor_shop,
            "vendor_category": vendor_category,
            "vendor_product": vendor_product,
            "client_products": client_products,
        },
    )


class SignUpView(TemplateView):
    template_name = "registration/signup.html"


class UserListView(UserPassesTestMixin, ListView):
    """admin sees all users"""

    model = User
    template_name = "users_list.html"
    paginate_by = 6

    def test_func(self):
        return self.request.user.is_staff


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/user_detail.html"

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)


# Client views
class ClientSignUpView(SuccessMessageMixin, CreateView):
    model = User
    form_class = ClientCreationForm
    template_name = "registration/signup_form.html"
    success_message = "Account Created Successfully"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "client"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("accounts:dashboard")


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = "accounts/user_profile.html"
    context_object_name = "client_detail"

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)


class ClientUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Client
    template_name = "accounts/user_update.html"
    success_message = "Profile Updated Successfully!"
    fields = [
        "image",
        "phone_number",
        "location",
    ]
    success_url = reverse_lazy("accounts:dashboard")

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    # def get_success_url(self) -> str:
    #     return reverse_lazy("accounts:client-profile", kwargs={"pk": self.object.pk})


# Vendor views
class VendorSignUpView(SuccessMessageMixin, CreateView):
    model = User
    form_class = VendorCreationForm
    template_name = "registration/signup_form.html"
    success_message = "Account Created Successfully"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "vendor"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("accounts:dashboard")


class VendorDetailView(LoginRequiredMixin, DetailView):
    model = Vendor
    template_name = "accounts/user_profile.html"
    context_object_name = "vendor_detail"

    def get_queryset(self):
        return Vendor.objects.filter(user=self.request.user)


class VendorUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Vendor
    template_name = "accounts/user_update.html"
    success_message = "Profile Updated Successfully!"
    fields = [
        "image",
        "phone_number",
        "shop_location",
    ]
    success_url = reverse_lazy("accounts:dashboard")

    def get_queryset(self):
        return Vendor.objects.filter(user=self.request.user)

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    # def get_success_url(self) -> str:
    #     return super().get_success_url() or reverse_lazy(
    #         "accounts:vendor-profile", kwargs={"pk": self.object.pk}
    #     )


# Admin Views
class AdminSignUpView(SuccessMessageMixin, CreateView):
    model = User
    form_class = AdminCreationForm
    template_name = "registration/signup_form.html"
    success_message = "Account Created Successfully"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "admin"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("accounts:dashboard")


class AdminDetailView(LoginRequiredMixin, DetailView):
    model = Admin
    template_name = "accounts/user_profile.html"

    def get_queryset(self):
        return Admin.objects.filter(user=self.request.user)


class AdminUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Admin
    fields = ["image"]
    template_name = "accounts/user_update.html"
    success_message = "Profile Updated Successfully!"

    def get_queryset(self):
        return Admin.objects.filter(user=self.request.user)

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy("accounts:admin-profile", kwargs={"pk": self.object.pk})
