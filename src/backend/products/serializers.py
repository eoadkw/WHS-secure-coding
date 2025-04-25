from rest_framework import serializers
from .models import Product, ProductReport

class ProductSerializer(serializers.ModelSerializer):
    seller_username = serializers.CharField(source='seller.username', read_only=True)
    likes_count     = serializers.IntegerField(source='likes.count', read_only=True)
    reports_count   = serializers.IntegerField(source='reports.count', read_only=True)

    class Meta:
        model  = Product
        fields = ['id','title','description','price','created_at',
                  'seller','seller_username',
                  'likes_count','reports_count']

class ProductReportSerializer(serializers.ModelSerializer):
    reporter_username = serializers.CharField(source='reporter.username', read_only=True)

    class Meta:
        model  = ProductReport
        fields = ['id','reporter','reporter_username','product','reason','created_at']

