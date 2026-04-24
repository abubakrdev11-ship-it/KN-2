from rest_framework import generics, mixins, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Product
from .serializers import ProductSerializer
from apps.user.permissions import IsOwnerOrReadOnly, IsSeller

class RootAPIView(APIView):
    def get(self, request):
        return Response({"message": "Marketplace API"})

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.select_related('category', 'seller').all()
    serializer_class = ProductSerializer
    filterset_fields = ['category']
    ordering_fields = ['price', 'created_at']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsSeller()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]