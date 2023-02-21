import requests
from random import choice
from collections import OrderedDict
from elasticsearch import TransportError, ConnectionError

from app.schemas import Product
from app.clients.es import es_client
from app.enums import Indexes
from app.crawlers.user_agents import AGENT_LIST


class Base:
    """
    Base class for all crawlers
    """

    @staticmethod
    def get_user_agent():
        """
        Get random User-Agent header
        """
        user_agent = choice(AGENT_LIST)
        return user_agent

    headers = OrderedDict({
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;q=0.9,"
            "image/avif,image/webp,*/*;q=0.8"
        ),
        "Accept-Encoding": "gzip, deflate, utf-8",
        "Accept-Language": "en-US,en;q=0.5",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "DNT": "1",
        "User-Agent": get_user_agent(),
        "Upgrade-Insecure-Requests": "1",
    })

    def request(self, url: str, headers: dict) -> str:
        """
        HTTP request method
        """
        headers.update(self.headers)
        try:
            response = requests.get(url=url, headers=self.headers).text
        except (requests.RequestException, requests.ConnectionError):
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
