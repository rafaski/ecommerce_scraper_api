from bs4 import BeautifulSoup
from collections import OrderedDict

from app.schemas import Product
from app.crawlers.base_crawler import Base


class Xkom:
    """
    A crawler class that supports product data scraping from x-kom.pl domain
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

    def parse(self, url: str) -> dict:
        """
        Scrape product data from website and save results to elasticsearch
        """
        # get a html text file
        response = Base().request(url=url, headers=self.headers)

        doc = BeautifulSoup(response, "html.parser")

        # extract data from response
        name = doc.find(class_="sc-1bker4h-4 hMQkuz").text
        price_currency_str = doc.find(class_="sc-n4n86h-4 jwVRpW").text
        price = int(price_currency_str.split(",")[0].replace(" ", ""))
        currency = price_currency_str.split(" ")[-1][-2:]
        average_rating = doc.find(
            class_="sc-1h16fat-0 sc-1ngc1lj-1 eKEFnB sc-1bker4h-6 gDIfGT"
        )
        average_rating = float(average_rating["title"][-4:])
        review_count = doc.find(class_="sc-1ngc1lj-2 eJPDue").text
        review_count = int(review_count.split(" ")[0][1:])
        all_reviews = doc.find_all(
            class_="sc-u1peis-1 etZjkD sc-s2qgtg-21 gIUavP"
        )
        reviews = []
        for review in all_reviews:
            reviews.append(review.text)

        product = Product(
            name=name,
            price=price,
            currency=currency,
            review_count=review_count,
            average_rating=average_rating,
            reviews=reviews,
            url=url
        )
        Base().save(product=product)

        return product.dict()
