from django.contrib import admin

from shop.models import Shop, Product, Order

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Order)
