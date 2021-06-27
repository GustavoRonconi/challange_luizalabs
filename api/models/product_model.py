from django.db import models


class ProductModel(models.Model):
    class Meta:
        db_table = "product"

    id = models.UUIDField(primary_key=True, editable=False)

    product_url = models.URLField(blank=True)

