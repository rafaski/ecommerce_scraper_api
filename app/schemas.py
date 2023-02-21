from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


class Review(BaseModel):
    """
    Review schema
    """
    name: str
    review: str
    date: datetime


class Product(BaseModel):
    """
    Product schema
    """
    name: str
    price: int
    currency: str
    review_count: int
    average_rating: float
    reviews: List[Review]
    url: str


class Output(BaseModel):
    """
    Output schema
    """
    success: bool
    message: Optional[str] = None
    result: Optional[Product] = None
