from django.contrib import admin
from .models import Product, ProductReport

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display  = ['id', 'seller', 'title', 'price', 'status', 'created_at']
    list_filter   = ['status', 'seller']
    search_fields = ['title', 'description']

@admin.register(ProductReport)
class ProductReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'reporter', 'product', 'reason', 'created_at']
    list_filter  = ['product', 'reporter']

