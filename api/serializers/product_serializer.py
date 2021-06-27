from rest_framework import serializers
from api.models.product_model import ProductModel

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    product_url = serializers.URLField(read_only=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=5, read_only=True)
    brand = serializers.CharField(read_only=True)
    title = serializers.CharField(read_only=True)
    image = serializers.URLField(read_only=True)

    class Meta:
        model = ProductModel
        fields = ("id", "product_url", "price", "brand", "title", "image")