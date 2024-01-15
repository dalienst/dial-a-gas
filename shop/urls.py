from django.urls import path

from shop.views import ShopUpdateView

app_name = "shop"

urlpatterns = [
    path("update/<str:pk>/shop/", ShopUpdateView.as_view(), name="shop-update"),
]
