import tldextract


def get_host(url: str):
    result = tldextract.extract(url=url)
    return result.domain.replace("-", "")
