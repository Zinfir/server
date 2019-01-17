from product_detail.models import Product
from rest_framework.viewsets import ModelViewSet
from product_detail.serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(special_offer='Trending')
    serializer_class = ProductSerializer