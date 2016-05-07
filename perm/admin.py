from django.contrib import admin

from .models import Perm


@admin.register(Perm)
class AssetAdmin(admin.ModelAdmin):
    pass
