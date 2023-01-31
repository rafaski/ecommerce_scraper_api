import requests
from elasticsearch import TransportError, ConnectionError

from app.schemas import Product
from app.clients.es import es_client
from app.enums import Indexes


class Base:
    """
    Base class for all crawlers
    """

    def request(self, url: str, headers: dict) -> str:
        """
        HTTP request method
        """
        try:
            response = requests.get(url=url, headers=headers).text
        except requests.ConnectionError:
            raise
        return response

    @staticmethod
    def save(product: Product) -> None:
        """
        Save results to elastic search
        """
        try:
            es_client.index(
                index=Indexes.PROFILES_V2,
                id=product.url,
                document=product.dict()
            )
        except (TransportError, ConnectionError):
            raise
