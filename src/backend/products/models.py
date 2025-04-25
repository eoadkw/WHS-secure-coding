from django.db import models
from django.conf import settings

class Product(models.Model):
    title        = models.CharField(max_length=100)
    description  = models.TextField(blank=True)
    price        = models.PositiveIntegerField()
    created_at   = models.DateTimeField(auto_now_add=True)
    seller       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    likes        = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='liked_products')

    def __str__(self):
        return f"{self.title} - {self.price}원"

class ProductReport(models.Model):
    reporter   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports_made')
    product    = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reports')
    reason     = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

