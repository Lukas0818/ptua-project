from django.contrib import admin
from .models import Category, Service, UserRentService

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'type', 'category', 'stock']
    list_filter = ['type']

admin.site.register(Category)
admin.site.register(Service, ServiceAdmin)
admin.site.register(UserRentService)