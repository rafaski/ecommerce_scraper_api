from bs4 import BeautifulSoup
from collections import OrderedDict
import requests

from app.schemas import Product
from app.clients.es import es_client


class Xkom:
    """
    TBA
    """
    headers = {
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;q=0.9,"
            "image/avif,image/webp,*/*;q=0.8"
        ),
        "Accept-Encoding": "gzip, deflate, utf-8",
        "Accept-Language": "en-US,en;q=0.5",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "www.x-kom.pl",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) "
            "Gecko/20100101 Firefox/110.0"
        )
    }
    headers = OrderedDict(headers)

    def request(self, url: str):
        response = requests.get(url=url, headers=self.headers).text
        return response

    def parse(self, url: str):
        response = self.request(url=url)

        doc = BeautifulSoup(response, "html.parser")
        name = doc.find(class_="sc-1bker4h-4 hMQkuz").text
        price = doc.find(class_="sc-n4n86h-4 jwVRpW").text
        review_count = doc.find(class_="sc-1ngc1lj-2 eJPDue").text
        review_count = int(review_count.split(" ")[0][1:])

        product = Product(
            name=name,
            review_count=review_count,
            url=url
        )
        self.save(product=product)

        return product.dict()

    @staticmethod
    def save(product: Product):

        es_client.index(
            index="profiles-v1",
            id=product.url,
            document=product.dict()
        )

    # TODO proper schema, error handling, abstract methods into Base class,
    # TODO check elasticsearch before scraping, move into settings
    # TODO pytest


