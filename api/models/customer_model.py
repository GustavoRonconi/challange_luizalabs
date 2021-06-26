from django.db import models


class CustomerModel(models.Model):
    class Meta:
        db_table = "customer"

    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField(max_length=254)

