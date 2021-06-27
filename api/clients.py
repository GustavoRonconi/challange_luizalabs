from uuid import uuid4
import requests

URL_CHALLANGE_API = "http://challenge-api.luizalabs.com/api/product/"


class ChallangeApi:
    def __init__(self, uuid: uuid4) -> None:
        self.product_url = URL_CHALLANGE_API + str(uuid) + "/"

    @property
    def product_challange_api(self) -> dict:
        response = requests.get(self.product_url)
        if response.status_code == 404:
            return
        return {**response.json(), "product_url": self.product_url}
