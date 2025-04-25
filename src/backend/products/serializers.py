# src/backend/products/serializers.py

from rest_framework import serializers
from .models import Product, Report

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'owner', 'title', 'description', 'price', 'likes', 'created_at']
        read_only_fields = ['id', 'owner', 'created_at', 'likes']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'reporter', 'product', 'reason', 'created_at']
        read_only_fields = ['id', 'reporter', 'created_at']

