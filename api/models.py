from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

class BookOut(BaseModel):
    title: str
    price: float
    scraped_at: datetime
    url: str

class StatsOut(BaseModel):
    total_books: int
    avg_price: float
    min_price: float
    max_price: float
    last_scraped: datetime

class QueryParams(BaseModel):
    limit: int = Field(20, ge=1, le=100, description="Макс. кол-во записей (1-100)")
    offset: int = Field(0, ge=0, description="Смещение для пагинации")
    sort_by: Literal["price", "scraped_at", "title"] = "price"
    order: Literal["asc", "desc"] = "desc"
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    title_contains: Optional[str] = None