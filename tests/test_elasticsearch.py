from app.clients.es import es_client
from app.crawlers.xkom import Xkom
from app.enums import Indexes

URL = (
    "https://www.x-kom.pl/p/1054822-notebook-laptop-133-apple-"
    "macbook-air-m2-16gb-256-mac-os-midnight.html#Specyfikacja"
)


def test_es() -> None:
    """
    Test elasticsearch
    """
    # parse data
    Xkom().parse(url=URL)

    result = es_client.get(index=Indexes.PROFILES_V2, id=URL)

    assert result.get("_id") == URL
