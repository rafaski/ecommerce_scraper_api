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

    # Create an index with an explicit mapping in elasticsearch API console
    elasticsearch_index_format = {
        "mappings": {
            "properties": {
                "name": {"type": "keyword"},
                "price": {"type": "integer"},
                "currency": {"type": "text"},
                "review_count": {"type": "integer"},
                "average_rating": {"type": "float"},
                "email": {"type": "keyword"},
                "reviews": {"type": "text"},
                "url": {"type": "text"}
            }
        }
    }
