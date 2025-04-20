from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings

class Product(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('selling', '판매중'),
        ('reserved', '예약중'),
        ('sold', '판매완료'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='selling')

    def __str__(self):
        return self.title

