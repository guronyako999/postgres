from django.db.models import Count
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """CRUD для категорий: /api/categories/"""

    permission_classes = [AllowAny]
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.annotate(products_count=Count('products'))


class ProductViewSet(viewsets.ModelViewSet):
    """CRUD для товаров: /api/products/ (фильтр ?category=<id>)"""

    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    queryset = Product.objects.select_related('category').all()

    def get_queryset(self):
        qs = super().get_queryset()
        category_id = self.request.query_params.get('category')
        if category_id:
            qs = qs.filter(category_id=category_id)
        return qs
