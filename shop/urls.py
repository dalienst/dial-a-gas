from django.urls import path

from shop.views import (
    ShopUpdateView,
    ShopDetailView,
    ShopListView,
    DeliveryCreateView,
    CategoryCreateView,
    ProductDetailView,
    ProductCreateView,
    ProductListView,
    ProductUpdateView,
)

app_name = "shop"

urlpatterns = [
    path("shops/", ShopListView.as_view(), name="shop-update"),
    path("update/<str:pk>/shop/", ShopUpdateView.as_view(), name="shop-update"),
    path("detail/<str:pk>/shop/", ShopDetailView.as_view(), name="shop-detail"),
    path("delivery/", DeliveryCreateView.as_view(), name="delivery-create"),
    path("category/", CategoryCreateView.as_view(), name="category-create"),
    path("create/", ProductCreateView.as_view(), name="product-create"),
    path(
        "product/<str:pk>/detail/", ProductDetailView.as_view(), name="product-detail"
    ),
    path(
        "product/<str:pk>/update/", ProductUpdateView.as_view(), name="product-update"
    ),
    path("products/", ProductListView.as_view(), name="product-list"),
]
