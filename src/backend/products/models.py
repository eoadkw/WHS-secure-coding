from django.db import models
from django.conf import settings

class Product(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    # 중개 모델 없이 기본 M2M
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_products',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Report(models.Model):
    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reports_made'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reports'
    )
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reporter.username} → {self.product.title}"

