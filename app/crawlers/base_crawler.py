import requests

from app.schemas import Product
from app.clients.es import es_client


class Base:
    """
    Base class for all crawlers
    """

    def request(self, url: str, headers: dict):
        """
        HTTP request method
        """
        response = requests.get(url=url, headers=headers).text
        return response

    @staticmethod
    def save(product: Product):
        """
        Save results to elastic search
        """
        es_client.index(
            index="profiles-v2",
            id=product.url,
            document=product.dict()
        )

    # Create an index with an explicit mapping in elasticsearch API console
    es_index = {
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
