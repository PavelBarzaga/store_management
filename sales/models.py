from django.db import models
from product.models import Product


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
