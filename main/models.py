from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    buying_price = models.IntegerField()
    selling_price = models.IntegerField()

    def profit(self):
        return self.buying_price - self.selling_price
