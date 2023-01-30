from typing import Optional, List
from pydantic import BaseModel


class Product(BaseModel):
    """
    Product schema
    """
    name: str
    price: int
    currency: str
    review_count: int
    average_rating: float
    reviews: List[str]
    url: str


class Output(BaseModel):
    """
    Output schema
    """
    success: bool
    message: Optional[str] = None
    result: Optional[Product] = None
