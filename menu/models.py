from django.db import models
import uuid

# Create your models here.
class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    productImg = models.ImageField(upload_to='product_images/')
    productTitle = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.CharField(max_length=10)
    color = models.JSONField()
    size = models.JSONField()
    stock = models.IntegerField()
    orders = models.IntegerField()
    publish = models.DateTimeField()

    def __str__(self):
        return f"{self.productTitle} - {self.category}"