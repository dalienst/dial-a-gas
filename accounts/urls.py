from django.urls import path

from accounts.views import (
    ClientSignUpView,
    ClientDetailView,
    ClientUpdateView,
    VendorDetailView,
    VendorUpdateView,
    VendorSignUpView,
    AdminSignUpView,
    AdminDetailView,
    AdminUpdateView,
    dashboard,
    SignUpView,
    UserListView,
    UserDetailView,
)

app_name = "accounts"

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("detail/<str:pk>/", UserDetailView.as_view(), name="user-detail"),
    # client urls
    path("sign-up/client/", ClientSignUpView.as_view(), name="client-signup"),
    path("profile/<str:pk>/client/", ClientDetailView.as_view(), name="client-profile"),
    path("update/<str:pk>/client/", ClientUpdateView.as_view(), name="client-update"),
    # vendor urls
    path("sign-up/vendor/", VendorSignUpView.as_view(), name="vendor-signup"),
    path("profile/<str:pk>/vendor/", VendorDetailView.as_view(), name="vendor-profile"),
    path("update/<str:pk>/vendor/", VendorUpdateView.as_view(), name="vendor-update"),
    # admin urls
    path("signup/admin/", AdminSignUpView.as_view(), name="admin-signup"),
    path("profile/<str:pk>/admin/", AdminDetailView.as_view(), name="admin-profile"),
    path("update/<str:pk>/admin/", AdminUpdateView.as_view(), name="admin-update"),
]
