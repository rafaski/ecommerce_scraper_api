from app.crawlers.xkom import Xkom

URL = (
    "https://www.x-kom.pl/p/1054822-notebook-laptop-133-apple-"
    "macbook-air-m2-16gb-256-mac-os-midnight.html#Specyfikacja"
)
NAME = "Apple MacBook Air M2/16GB/256/Mac OS Midnight"
PRICE = 6999
CURRENCY = "zł"


def test_xkom_crawler():
    """
    Test xkom product scraped data with expected result.
    """

    expected_result = {
        "name": NAME,
        "price": PRICE,
        "currency": CURRENCY
    }

    result = Xkom().parse(url=URL)

    assert expected_result.get("name") == result.get("name")
    assert expected_result.get("price") == result.get("price")
    assert expected_result.get("currency") == result.get("currency")
