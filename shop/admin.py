from django.contrib import admin

from shop.models import Shop, Product, Delivery, Category, Order

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Delivery)
admin.site.register(Category)
admin.site.register(Order)
