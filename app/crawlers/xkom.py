from typing import List

from bs4 import BeautifulSoup
from collections import OrderedDict
from elasticsearch import NotFoundError
from datetime import datetime

from app.enums import Indexes
from app.schemas import Product, Review
from app.crawlers.base_crawler import Base
from app.clients.es import es_client


class Xkom(Base):
    """
    A crawler class that supports product data scraping from x-kom.pl domain
    """

    headers_ = OrderedDict({
        "Host": "www.x-kom.pl"
    })

    def parse(self, url: str) -> dict:
        """
        Scrape product data from website and save results to elasticsearch
        """
        # check elasticsearch before scraping http request
        # try:
        #     doc = es_client.get(index=Indexes.PROFILES_V2, id=url)
        #     return doc.get("_source")
        # except NotFoundError:
        #     pass

        # get a html text file
        response = self.request(url=url, headers=self.headers_)

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
            class_="sc-1s1zksu-0 sc-1s1zksu-1 hHQkLn sc-s2qgtg-20 hTjidB"
        )
        reviews: List[Review] = []
        for item in all_reviews:
            reviewer = item.find(class_="sc-s2qgtg-0 kZKWrI").text
            date = item.find(class_="sc-s2qgtg-10 ia-ddoT").get("title")
            date = datetime.strptime(date, '%d-%m-%Y | %H:%M')
            # review = item.find(
            #     class_="sc-u1peis-1 jlprMD sc-s2qgtg-21 gIUavP"
            # )
            # review = item.text
            # print(review)
            print(item.find(class_="sc-1s1zksu-0 eCLbtN sc-s2qgtg-19 fBPzZG").findChildren())
            # reviews.append(Review(name=reviewer, date=date, review=review))

        product = Product(
            name=name,
            price=price,
            currency=currency,
            review_count=review_count,
            average_rating=average_rating,
            reviews=reviews,
            url=url
        )
        # self.save(product=product)
        from pprint import pprint
        pprint(product.dict())
        return product.dict()


from pprint import pprint
var = Xkom().parse(url="https://www.x-kom.pl/p/1054822-notebook-laptop-133-apple-macbook-air-m2-16gb-256-mac-os-midnight.html#Specyfikacja")
pprint(var)


profile = {
  "profiles-v3": {
    "mappings": {
      "properties": {
        "review_count": {
          "type": "integer"
        },
        "name": {
          "type": "keyword"
        },
        "currency": {
          "type": "text"
        },
        "url": {
          "type": "text"
        },
        "price": {
          "type": "integer"
        },
        "reviews": {
          "type": "text"
        },
        "average_rating": {
          "type": "float"
        },
        "email": {
          "type": "keyword"
        }
      }
    }
  }
}

