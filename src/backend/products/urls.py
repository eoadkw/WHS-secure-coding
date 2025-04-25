from django.urls import path
from .views import (
    ProductListCreateView, ProductDetailView,
    toggle_like, report_product, ReportListView
)

urlpatterns = [
    path('products/',             ProductListCreateView.as_view()),
    path('products/<int:pk>/',    ProductDetailView.as_view()),
    path('products/<int:pk>/like/',   toggle_like),
    path('products/<int:pk>/report/', report_product),
    path('products/reports/',          ReportListView.as_view()),
]

