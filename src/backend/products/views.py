from rest_framework import generics, status, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, ProductReport
from .serializers import ProductSerializer, ProductReportSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class   = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends    = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields      = ['title','description']
    ordering_fields    = ['created_at','price']

    def get_queryset(self):
        qs = Product.objects.all()
        user     = self.request.user
        liked    = self.request.query_params.get('liked')
        reported = self.request.query_params.get('reported')
        if liked == 'true' and user.is_authenticated:
            qs = qs.filter(likes=user)
        if reported == 'true' and user.is_authenticated:
            qs = qs.filter(reports__reporter=user)
        return qs.order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset          = Product.objects.all()
    serializer_class  = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method in ['PUT','PATCH','DELETE']:
            return [IsAuthenticated()]
        return super().get_permissions()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_like(request, pk):
    product = Product.objects.filter(pk=pk).first()
    if not product: return Response({'error':'없음'}, status=404)
    user = request.user
    if user in product.likes.all():
        product.likes.remove(user); return Response({'message':'찜취소'})
    product.likes.add(user); return Response({'message':'찜추가'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def report_product(request, pk):
    product = Product.objects.filter(pk=pk).first()
    if not product: return Response({'error':'없음'}, status=404)
    if ProductReport.objects.filter(reporter=request.user, product=product).exists():
        return Response({'message':'이미신고'}, status=400)
    ProductReport.objects.create(
        reporter=request.user,
        product=product,
        reason=request.data.get('reason','')
    )
    return Response({'message':'신고완료'}, status=status.HTTP_201_CREATED)

class ReportListView(generics.ListAPIView):
    serializer_class   = ProductReportSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return ProductReport.objects.filter(reporter=self.request.user).order_by('-created_at')

