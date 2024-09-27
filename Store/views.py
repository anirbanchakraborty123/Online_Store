from rest_framework import viewsets
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """ CRUD views for Category Model"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    """ CRUD views for Product Model"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """ CRUD views for Order Model"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer