from django.contrib import admin
from .models import Product, Report

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'owner', 'created_at']
    list_filter = ['created_at', 'owner']
    search_fields = ['title', 'description']
    ordering = ['-created_at']


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'reporter', 'product', 'created_at']
    list_filter = ['created_at', 'reporter']
    search_fields = ['reason']
    ordering = ['-created_at']

