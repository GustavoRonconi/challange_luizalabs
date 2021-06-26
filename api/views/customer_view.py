from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models.customer_model import CustomerModel
from api.serializers.customer_serializer import CustomerModelSerializer


class CustomerView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        customers = CustomerModel.objects.all()
        serializer = CustomerModelSerializer(customers, many=True, context={"request": request})

        return Response(status=status.HTTP_200_OK, data=serializer.data)
