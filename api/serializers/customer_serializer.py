from rest_framework import serializers

from api.models.customer_model import CustomerModel


class CustomerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = "__all__"
