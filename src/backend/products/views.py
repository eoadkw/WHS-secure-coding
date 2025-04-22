from django.shortcuts import get_object_or_404
from rest_framework import status, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, ProductReport
from .serializers import ProductSerializer


# 상품 목록 조회 및 생성
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['price', 'seller', 'status']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'price']

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


# 상품 상세 조회, 수정, 삭제
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return []


# 찜 토글
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_like(request, pk):
    product = get_object_or_404(Product, pk=pk)
    user = request.user

    if user in product.likes.all():
        product.likes.remove(user)
        return Response({'message': '찜 취소됨'})
    else:
        product.likes.add(user)
        return Response({'message': '찜 추가됨'})


# 상품 신고
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def report_product(request, pk):
    user = request.user
    reason = request.data.get('reason', '')
    product = get_object_or_404(Product, pk=pk)

    if ProductReport.objects.filter(reporter=user, product=product).exists():
        return Response({'message': '이미 신고한 상품입니다'}, status=400)

    ProductReport.objects.create(reporter=user, product=product, reason=reason)

    if product.reports.count() > 3:
        product.is_active = False
        product.save()

    return Response({'message': '신고가 접수되었습니다'}, status=status.HTTP_201_CREATED)

def get_queryset(self):
    queryset = Product.objects.filter(is_active=True).order_by('-created_at')
    liked = self.request.query_params.get('liked')

    if liked == 'true' and self.request.user.is_authenticated:
        return queryset.filter(likes=self.request.user)
    return queryset

