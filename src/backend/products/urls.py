from django.urls import path
from .views import ProductListCreateView

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list-create'),
]

from django.urls import path
from .views import ProductListCreateView, ProductDetailView

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list-create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]

from .views import toggle_like

urlpatterns += [
    path('<int:pk>/like/', toggle_like, name='toggle-like'),
]

from .views import report_product

urlpatterns += [
    path('<int:pk>/report/', report_product, name='report-product'),
]

