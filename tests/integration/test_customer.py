import json

from uuid import UUID, uuid4

import pytest
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import force_authenticate


from api.models.customer_model import CustomerModel
from api.models.product_model import ProductModel
from api.serializers.customer_serializer import CustomerSerializer
from api.views.customer_view import CustomerView


@pytest.fixture
def valid_customer():
    products = [
        {
            "id": UUID("2b505fab-d865-e164-345d-efbd4c2045b6"),
            "product_url": "http://challenge-api.luizalabs.com/api/product/2b505fab-d865-e164-345d-efbd4c2045b6/",
        },
        {
            "id": UUID("9175d13b-52c6-f14c-05d1-f70f12e908b5"),
            "product_url": "http://challenge-api.luizalabs.com/api/product/9175d13b-52c6-f14c-05d1-f70f12e908b5/",
        },
    ]
    customer_dict = {"email": "gustavoronconi@teste.com.br", "name": "Gustavo A. Ronconi"}

    customer = CustomerModel.objects.create(**customer_dict)
    for p in products:
        product, _ = ProductModel.objects.get_or_create(**p)
        customer.products.add(product)

    customer_dict["id"] = str(customer.id)
    return {**customer_dict, "products": products}


@pytest.mark.parametrize(
    "as_view_option, valid_id", [("list", True), ("retrieve", True), ("retrieve", False)],
)
@pytest.mark.django_db
def test_get_customer(as_view_option, valid_id, factory, valid_user, valid_customer):
    id = uuid4()
    if valid_id:
        id = valid_customer["id"]

    factory_url = "/customer/"
    if as_view_option == "retrieve":
        factory_url = f"/customer/{id}/"
    serializer = CustomerSerializer(valid_customer)
    user = User.objects.get(username="gustavoronconi")
    view = CustomerView.as_view({"get": as_view_option})
    request = factory.get(factory_url)
    force_authenticate(request, user=user)
    response = view(request, pk=id)
    if not valid_id:
        assert response.status_code == status.HTTP_404_NOT_FOUND
        return
    if as_view_option == "list":
        assert json.dumps(response.data["results"]) == json.dumps([serializer.data])
        return
    assert json.dumps(response.data) == json.dumps(serializer.data)


@pytest.mark.django_db
@pytest.mark.parametrize(
    "customer, valid_payload",
    [
        ({"email": "gustavoronconi@teste1.com.br", "name": "Gustavo A. Ronconi",}, True,),
        (
            {
                "email": "gustavoronconi@teste2.com.br",
                "name": "Gustavo A. Ronconi",
                "products": [
                    {"id": "2b505fab-d865-e164-345d-efbd4c2045b6",},
                    {"id": "9175d13b-52c6-f14c-05d1-f70f12e908b5",},
                ],
            },
            True,
        ),
        (
            {
                "email": "gustavoronconi@teste3.com.br",
                "name": "Gustavo A. Ronconi",
                "products": [
                    {"id": "2b505fab-d865-e164-345d-efbd4c2045b6",},
                    {"id": "9175d13b-52c6-f14c-05d1-f70f12e908b5",},
                    {"id": "9175d13b-52c6-f14c-05d1-f70f12e908b5",},
                ],
            },
            False,
        ),
        (
            {
                "email": "gustavoronconi@teste2.com.br",
                "name": "Gustavo A. Ronconi",
                "products": [
                    {"id": "2b505fab-d865-e164-345d-efbd4c2045b7",},
                    {"id": "9175d13b-52c6-f14c-05d1-f70f12e908b5",},
                ],
            },
            False,
        ),
    ],
)
def test_post_customer(customer, valid_payload, valid_user, factory):
    user = User.objects.get(username="gustavoronconi")
    view = CustomerView.as_view({"post": "create"})
    request = factory.post("/customer/", json.dumps(customer), content_type="application/json",)

    force_authenticate(request, user=user)
    response = view(request)
    if valid_payload:
        assert response.status_code == status.HTTP_201_CREATED
        assert CustomerModel.objects.filter(email=customer["email"]).exists()
        return
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.parametrize(
    "customer, valid_payload",
    [
        ({"name": "Novo Nome"}, True),
        ({"products": [{"id": "35051d93-e0c1-cad3-b1d8-837e79be260e",}]}, True),
        ({"products": [{"id": "2b505fab-d865-e164-345d-efbd4c2045b7",}]}, False),
        ({"name": "Novo Nome 2", "products": [{"id": "2b505fab-d865-e164-345d-efbd4c2045b6",}]}, True),
    ],
)
@pytest.mark.django_db
def test_path_customer(customer, valid_payload, valid_customer, valid_user, factory):
    id = valid_customer["id"]
    user = User.objects.get(username="gustavoronconi")
    view = CustomerView.as_view({"patch": "partial_update"})
    request = factory.patch(f"/customer/{id}/", customer)
    force_authenticate(request, user=user)
    response = view(request, pk=id)

    if valid_payload:
        assert response.status_code == status.HTTP_200_OK
        if customer.get("name"):
            updated_customer = CustomerModel.objects.filter(name=customer["name"])
            assert updated_customer.exists()
            products = []
            if customer["name"] == "Novo Nome 2":
                for p in updated_customer.first().products.all():
                    assert str(p.id) not in products
        return
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_delete_customer(valid_customer, valid_user, factory):
    id = valid_customer["id"]
    user = User.objects.get(username="gustavoronconi")
    view = CustomerView.as_view({"delete": "destroy"})
    request = factory.delete(f"/customer/{id}/")
    force_authenticate(request, user=user)
    response = view(request, pk=id)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not CustomerModel.objects.filter(name=valid_customer["name"]).exists()

