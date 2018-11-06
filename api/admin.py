from django.contrib import admin

from .models import Pictures

class PicturesViewAdmin(admin.ModelAdmin):
	list_display = ("url_link", "description")

admin.site.register(Pictures, PicturesViewAdmin)