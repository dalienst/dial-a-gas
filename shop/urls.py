from django.urls import path

from shop.views import (
    ShopUpdateView,
    ShopDetailView,
    ShopListView,
    ProductDetailView,
    ProductCreateView,
    ProductListView,
    ProductUpdateView,
    OrderCreateView,
)

app_name = "shop"

urlpatterns = [
    path("shops/", ShopListView.as_view(), name="shop-update"),
    path("update/<str:pk>/shop/", ShopUpdateView.as_view(), name="shop-update"),
    path("detail/<str:pk>/shop/", ShopDetailView.as_view(), name="shop-detail"),
    path("create/", ProductCreateView.as_view(), name="product-create"),
    path(
        "product/<str:pk>/detail/", ProductDetailView.as_view(), name="product-detail"
    ),
    path(
        "product/<str:pk>/update/", ProductUpdateView.as_view(), name="product-update"
    ),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("order/<str:pk>/", OrderCreateView.as_view(), name="create-order")
]
