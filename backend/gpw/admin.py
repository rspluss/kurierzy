from django.contrib import admin
from .models import Index


@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    list_display = ['name', 'number']
