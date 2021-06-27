import uuid

from django.db import models


class CustomerModel(models.Model):
    class Meta:
        db_table = "customer"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    products = models.ManyToManyField("ProductModel", related_name="products", blank=True)
