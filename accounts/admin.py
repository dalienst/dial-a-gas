from django.contrib import admin
from django.contrib.auth import get_user_model

from accounts.models import Admin, Client, Vendor

User = get_user_model()

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Client)
admin.site.register(Vendor)
