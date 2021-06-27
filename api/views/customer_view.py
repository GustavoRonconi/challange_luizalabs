from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.models.customer_model import CustomerModel
from api.serializers.customer_serializer import CustomerSerializer


# TODO paginar
class CustomerView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSerializer
    ilter_backends = [OrderingFilter]
