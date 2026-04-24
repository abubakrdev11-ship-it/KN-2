from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'stock', 'category', 'seller', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('category', 'seller')