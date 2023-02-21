from celery import Celery
from importlib import import_module
import requests

from app.utils import get_host
from app.settings import BROKER_URL, RESULT_BACKEND, TASK_DEFAULT_QUEUE

"""
Create a celery app, queue and tasks
"""

celery_app = Celery(main="celery_app")
celery_app.conf.task_default_queue = TASK_DEFAULT_QUEUE
celery_app.conf.broker_url = BROKER_URL
celery_app.conf.result_backend = RESULT_BACKEND


@celery_app.task
def run_crawler(url: str, callback_url: str) -> None:
    """
    Identify url host name, import module with a corresponding crawler
    based on supported host name, run a crawler (parse data from url),
    send payload (extracted data by crawler) to client's callback url.
    """
    host = get_host(url=url)
    module = import_module(name=f"app.crawlers.{host}")
    crawler = getattr(module, host.capitalize())
    result = crawler().parse(url=url)
    send_callback(url=callback_url, payload=result)


def send_callback(url: str, payload: dict) -> None:
    """
    Send payload (extracted data by crawler) to client's callback url.
    """
    try:
        requests.post(url=url, data=payload)
    except (requests.exceptions.InvalidURL, requests.HTTPError):
        raise

    # TODO Create a Celery task out of this function and enqueue that into a separate queue called callbacks
