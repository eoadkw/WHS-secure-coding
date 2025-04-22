from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Product, ProductReport

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'seller', 'price', 'status', 'created_at', 'is_active']
    list_filter = ['status', 'is_active', 'created_at']
    search_fields = ['title', 'description', 'seller__username']

@admin.register(ProductReport)
class ProductReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'reporter', 'product', 'created_at']
    search_fields = ['reporter__username', 'product__title']

