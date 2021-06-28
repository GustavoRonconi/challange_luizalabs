from uuid import UUID
from unittest import mock
from api.clients import ChallangeApi
import pytest


@pytest.mark.parametrize(
    "product_id, status_code, mocked_response, expected_result",
    [
        (
            UUID("2b505fab-d865-e164-345d-efbd4c2045b6"),
            200,
            {"a": 1, "b": 2},
            {
                "a": 1,
                "b": 2,
                "product_url": "http://challenge-api.luizalabs.com/api/product/2b505fab-d865-e164-345d-efbd4c2045b6/",
            },
        ),
        (UUID("2b505fab-d865-e164-345d-efbd4c2045b7"), 404, None, None),
    ],
)
@mock.patch("api.clients.requests.get")
def test_product_challange_api(mock_requests_get, product_id, status_code, mocked_response, expected_result):
    challange_api = ChallangeApi(product_id)

    class MockResponse:
        def __init__(self, status_code, mocked_response):
            self.status_code = status_code
            self.mocked_response = mocked_response

        def json(self):
            return self.mocked_response

    mock_requests_get.return_value = MockResponse(status_code, mocked_response)
    assert challange_api.product_challange_api == expected_result
