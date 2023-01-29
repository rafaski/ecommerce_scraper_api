import os
from typing import Any
from dotenv import load_dotenv

load_dotenv()


def load_variable(name: str, default: Any = None) -> str:
    variable = os.getenv(name, default)
    if variable is None:
        print(f"Unable to load variable {name}")
    return variable


# elasticsearch
ELASTICSEARCH_CLOUD_ID = load_variable(name="ELASTICSEARCH_CLOUD_ID")
ELASTICSEARCH_PASSWORD = load_variable(name="ELASTICSEARCH_PASSWORD")
