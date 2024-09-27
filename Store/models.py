from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """ Category Model with fields name and description """

    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        """ Returns category name""" 
        return f"{self.name}"

class Product(models.Model):
    """ Product Model with fields name, description, price, category, stock"""

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    stock = models.PositiveIntegerField()

    def __str__(self):
        """ Returns category name"""
        return f"{self.name}"

class Order(models.Model):
    """ Order Model with fields user, products, total_amount, created_at"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Returns order id followed by the user""" 
        return f"Order {self.id} by {self.user}"
