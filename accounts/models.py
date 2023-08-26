from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=100, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    profile_image = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):

    CATEGORY = (
        ('In door', 'In door'),
        ('Out door', 'Out door')
    )

    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=200, decimal_places=2, null=True)
    category = models.CharField(max_length=200, choices=CATEGORY, null=True)
    description = models.TextField(null=True, blank=True)
    tag = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out of delivery', 'Out of delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, choices=STATUS, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.product.name