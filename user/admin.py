from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UserViewAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in User._meta.get_fields() ]

admin.site.register(User, UserViewAdmin)