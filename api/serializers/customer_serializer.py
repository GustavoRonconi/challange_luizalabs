from copy import deepcopy

from rest_framework import serializers

from api.models.customer_model import CustomerModel
from api.models.product_model import ProductModel
from api.clients import ChallangeApi


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


class CustomerSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = CustomerModel
        fields = "__all__"
        extra_kwargs = {"products": {"required": False}}

    def to_representation(self, instance):
        response = super(CustomerSerializer, self).to_representation(instance)
        for p in response["products"]:
            challange_api = ChallangeApi(p["id"])
            p.update(challange_api.product_challange_api)
        return response

    def validate(self, data):
        for p in data["products"]:
            challange_api = ChallangeApi(p["id"])
            product = challange_api.product_challange_api
            if not product:
                raise serializers.ValidationError({"products": f"""Produto inexistente: {p["id"]}"""})
            p.update(product)
        return data

    def create(self, validated_data):
        initial_validated_data = deepcopy(validated_data)
        products = validated_data.pop("products")
        customer = CustomerModel.objects.create(**validated_data)
        for p in products:
            keys_to_remove = ["price", "brand", "title", "image"]
            for k in keys_to_remove:
                del p[k]
            product, _ = ProductModel.objects.get_or_create(**p)
            product.save()
            customer.products.add(product)
        customer.save()

        return initial_validated_data
