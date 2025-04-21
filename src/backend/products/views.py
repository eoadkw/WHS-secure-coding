from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        products = Product.objects.all().order_by('-created_at')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(seller=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return []

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['price', 'seller', 'status' ]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['price']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'price']

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_like(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': '상품이 존재하지 않습니다'}, status=404)

    user = request.user
    if user in product.likes.all():
        product.likes.remove(user)
        return Response({'message': '찜 취소됨'})
    else:
        product.likes.add(user)
        return Response({'message': '찜 추가됨'})

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import ProductReport

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def report_product(request, pk):
    user = request.user
    reason = request.data.get('reason', '')
    
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': '상품이 존재하지 않습니다'}, status=404)

    # 이미 신고한 경우 방지
    if ProductReport.objects.filter(reporter=user, product=product).exists():
        return Response({'message': '이미 신고한 상품입니다'}, status=400)

    ProductReport.objects.create(reporter=user, product=product, reason=reason)
    return Response({'message': '신고가 접수되었습니다'}, status=status.HTTP_201_CREATED)

