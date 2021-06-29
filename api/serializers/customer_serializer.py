from copy import deepcopy

from rest_framework import serializers

from api.models.customer_model import CustomerModel
from api.models.product_model import ProductModel
from api.serializers.product_serializer import ProductSerializer
from api.clients import ChallengeApi


class CustomerSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, required=False, default=[])

    class Meta:
        model = CustomerModel
        fields = "__all__"

    def to_representation(self, instance):
        response = super(CustomerSerializer, self).to_representation(instance)
        for p in response["products"]:
            challenge_api = ChallengeApi(p["id"])
            p.update(challenge_api.product_challenge_api)
        return response

    def remove_keys(self, data_dict):
        keys_to_remove = ["price", "brand", "title", "image"]
        for k in keys_to_remove:
            del data_dict[k]
        return data_dict

    def validate(self, data):
        products = []
        if not data.get("products"):
            return data
        for p in data["products"]:
            challenge_api = ChallengeApi(p["id"])
            product = challenge_api.product_challenge_api
            if not product:
                raise serializers.ValidationError({"products": f"""Produto inexistente: {p["id"]}"""})
            if p["id"] in products:
                raise serializers.ValidationError({"products": f"""Produto duplicado: {p["id"]}"""})
            products.append(p["id"])
            p.update(product)
        return data

    def create(self, validated_data):
        initial_validated_data = deepcopy(validated_data)
        products = validated_data.pop("products")
        customer = CustomerModel.objects.create(**validated_data)
        for p in products:
            p = self.remove_keys(p)
            product, _ = ProductModel.objects.get_or_create(**p)
            product.save()
            customer.products.add(product)
        customer.save()

        return initial_validated_data

    def update(self, instance, validated_data):
        products = validated_data.get("products", [])
        if products:
            products = validated_data.pop("products")

        for k, v in validated_data.items():
            setattr(instance, k, v)

        for p in products:
            p = self.remove_keys(p)
            product, _ = ProductModel.objects.get_or_create(**p)
            instance.products.add(product)
        instance.save()
        return instance
