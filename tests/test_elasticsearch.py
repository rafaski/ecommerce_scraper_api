from app.clients.es import es_client
from app.crawlers.xkom import Xkom

URL = (
    "https://www.x-kom.pl/p/1054822-notebook-laptop-133-apple-"
    "macbook-air-m2-16gb-256-mac-os-midnight.html#Specyfikacja"
)
INDEX = "profiles-v2"


def test_es():
    """
    Test elasticsearch
    """
    # parse data
    Xkom().parse(url=URL)

    result = es_client.get(index=INDEX, id=URL)

    assert result.get("_id") == URL
