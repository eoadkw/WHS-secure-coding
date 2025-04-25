# backend/src/backend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views    import RegisterView
from products.views import ProductViewSet, ReportViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'reports',  ReportViewSet,  basename='report')

urlpatterns = [
    path('admin/',                  admin.site.urls),
    path('api/auth/register/',      RegisterView.as_view(),      name='register'),
    path('api/auth/login/',         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(),   name='token_refresh'),
    path('api/',                    include(router.urls)),
]
# backend/src/backend/urls.py
