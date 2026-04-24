from django.contrib import admin
from .models import Order

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'product', 'quantity', 'total_price', 'created_at')
    list_filter = ('buyer', 'product', 'created_at')
    search_fields = ('buyer__username', 'product__name')