import pytest
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


from rest_framework.test import APIRequestFactory


@pytest.fixture(scope="session")
def factory():
    return APIRequestFactory()


@pytest.fixture
def valid_user():
    valid_user = {
        "username": "gustavoronconi",
        "password": make_password("gustavoronconi"),
        "email": "gustavo.ronconi@gmail.com.br",
        "first_name": "Gustavo A.",
        "last_name": "Ronconi",
        "is_staff": True,
    }
    User.objects.create(**valid_user)
    return valid_user
