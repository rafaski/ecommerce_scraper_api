import tldextract


def get_host(url: str) -> str:
    """
    Util function that returns url domain as string
    """
    result = tldextract.extract(url=url)
    return result.domain.replace("-", "")
