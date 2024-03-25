from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.IntegerField()
    amount_display = models.IntegerField()
    amount_stored = models.IntegerField()
