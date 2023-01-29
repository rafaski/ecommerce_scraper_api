from celery import Celery
from importlib import import_module
import requests

from app.utils import get_host

celery_app = Celery(main="celery_app")
celery_app.conf.task_default_queue = "test"
celery_app.conf.broker_url = "redis://localhost:6379/0"
celery_app.conf.result_backend = "redis://localhost:6379/0"


@celery_app.task
def run_crawler(url: str, callback_url: str):
    host = get_host(url=url)
    module = import_module(name=f"app.crawlers.{host}")
    crawler = getattr(module, host.capitalize())
    result = crawler().parse(url=url)
    send_callback(url=callback_url, payload=result)


def send_callback(url: str, payload: dict):
    requests.post(url=url, data=payload)
