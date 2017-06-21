from django.contrib import admin

# Register your models here.

from .models import Asset


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    pass
