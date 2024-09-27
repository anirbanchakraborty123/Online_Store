# Standard library imports
import pytest
# Third-party imports
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
# Local application imports
from .models import Category, Product


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    return User.objects.create_user(username='testuser', password='password')

@pytest.fixture
def create_category():
    return Category.objects.create(name="Electronics", description="Electronic items")

@pytest.fixture
def create_product(create_category):
    return Product.objects.create(name="Laptop", description="A gaming laptop", price=1000, category=create_category, stock=10)

@pytest.mark.django_db
def test_product_creation(api_client, create_product):
    url = reverse('product-list')
    response = api_client.post(url, {
        'name': 'Phone',
        'description': 'A smartphone',
        'price': 500,
        'category': create_product.category.id,
        'stock': 5
    })
    assert response.status_code == 201

@pytest.mark.django_db
def test_order_creation_with_insufficient_stock(api_client, create_user, create_product):
    api_client.force_authenticate(user=create_user)
    create_product.stock = 0
    create_product.save()

    url = reverse('order-list')
    response = api_client.post(url, {
        'user': create_user.id,
        'products': [create_product.id]
    })

    assert response.status_code == 400
    assert "out of stock" in str(response.data)

@pytest.mark.django_db
def test_crud_product(api_client, create_category):
    response = api_client.post('/v1/api/products/', {
        'name': 'Laptop', 'description': 'Gaming Laptop', 'price': 1499.99, 'category': create_category.id, 'stock': 5
    }, format='json')

    assert response.status_code == 201
    product_id = response.data['id']

    # Test GET
    response = api_client.get(f'/v1/api/products/{product_id}/')
    assert response.status_code == 200

    # Test PUT
    response = api_client.put(f'/v1/api/products/{product_id}/', {
        'name': 'Updated Laptop', 'description': 'Updated Description', 'price': 1599.99, 'category': create_category.id, 'stock': 4
    }, format='json')
    assert response.status_code == 200

    # Test DELETE
    response = api_client.delete(f'/v1/api/products/{product_id}/')
    assert response.status_code == 204
    
@pytest.mark.django_db
def test_create_order(api_client, create_user, create_product):
    api_client.force_authenticate(user=create_user)
    response = api_client.post('/v1/api/orders/', {
        'user': create_user.id,
        'products': [create_product.id]
    }, format='json')

    assert response.status_code == 201
    create_product.refresh_from_db()
    assert create_product.stock == 9  # Stock should be reduced after order