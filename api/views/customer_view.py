from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.models.customer_model import CustomerModel
from api.serializers.customer_serializer import CustomerSerializer


class CustomerView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = CustomerModel.objects.all().order_by("id")
    serializer_class = CustomerSerializer
