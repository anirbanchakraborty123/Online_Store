from rest_framework import serializers
from .models import Category, Product, Order

class CategorySerializer(serializers.ModelSerializer):
    """ CategorySerializer to serialize Category Model """

    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    """ ProductSerializer to serialize Product Model """

    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    """ OrderSerializer to serialize Order Model """

    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def validate(self, attrs):
        """ Check product stock availability and return data """

        # Check product stock availability
        for product in attrs['products']:
            if product.stock <= 0:
                raise serializers.ValidationError(f" Product {product.name} is out of stock.")
        return attrs

    def create(self, validated_data):
        """ Create and return order data """

        products = validated_data.pop('products')
        total_amount = sum(product.price for product in products)

        order = Order.objects.create(total_amount=total_amount, **validated_data)
        order.products.set(products)

        # Decrement stock
        for product in products:
            if product.stock < 1:
                raise serializers.ValidationError(f"Insufficient stock for {product.name}")
            product.stock -= 1
            product.save()

        return order
