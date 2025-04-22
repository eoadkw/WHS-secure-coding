from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

class Product(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    likes = models.ManyToManyField(User, related_name='liked_products', blank=True)

    STATUS_CHOICES = [
        ('selling', '판매중'),
        ('reserved', '예약중'),
        ('sold', '판매완료'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='selling')

    def __str__(self):
        return self.title

class ProductReport(models.Model):
    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reports'
    )
    reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('reporter', 'product')  # 동일 유저는 같은 상품 중복 신고 불가

    def __str__(self):
        return f'{self.reporter} → {self.product}'

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

