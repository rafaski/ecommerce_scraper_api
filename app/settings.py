import os
from typing import Any
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()


@lru_cache()
def load_variable(name: str, default: Any = None) -> str:
    variable = os.getenv(name, default)
    if variable is None:
        print(f"Unable to load variable {name}")
    return variable


# api key
API_KEY = load_variable(name="API_KEY")

# elasticsearch
ELASTICSEARCH_CLOUD_ID = load_variable(name="ELASTICSEARCH_CLOUD_ID")
ELASTICSEARCH_PASSWORD = load_variable(name="ELASTICSEARCH_PASSWORD")

# celery app
BROKER_URL = load_variable(
    name="BROKER_URL",
    default="redis://localhost:6379/0"
)
RESULT_BACKEND = load_variable(
    name="RESULT_BACKEND",
    default="redis://localhost:6379/0"
)
TASK_DEFAULT_QUEUE = load_variable(
    name="TASK_DEFAULT_QUEUE",
    default="crawling"
)
