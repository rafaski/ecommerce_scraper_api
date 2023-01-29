from typing import Optional
from pydantic import BaseModel


class Price(BaseModel):
    """
    TBA
    """
    amount: int
    currency: str


class Product(BaseModel):
    """
    TBA
    """
    name: str
    # price: Price
    review_count: int
    # average_rating: float
    url: str


class Output(BaseModel):
    """
    TBA
    """
    success: bool
    message: Optional[str] = None
    result: Optional[Product] = None
