from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Post


class PostViewAdmin(admin.ModelAdmin):
	list_display = [ field.name for field in Post._meta.get_fields() ]

admin.site.register(Post, PostViewAdmin)