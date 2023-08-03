from django.contrib import admin
from .models import Category, Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'type', 'category', 'stock']
    list_filter = ['type']

admin.site.register(Category)
admin.site.register(Service, ServiceAdmin)