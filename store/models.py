from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='books', null=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    image_url = models.URLField()
    created_date = models.DateField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.book_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='products', null=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image_url = models.URLField()
    created_date = models.DateField()
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.product_name
   

class Cart(models.Model):
    cart_id = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    books = models.ManyToManyField(Book)
    product = models.ManyToManyField(Product)

    class Meta:
        ordering = ['cart_id', '-created_at']

    def __str__(self):
        return f'{self.cart_id}'
    