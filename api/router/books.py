from fastapi import APIRouter, Query, Depends
from typing import Optional
from api.dependecies import load_books
from api.models import BookOut, StatsOut, QueryParams
import pandas as pd

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=list[BookOut])
def get_books(q: QueryParams = Depends()):
    df = load_books()
    
    # Фильтры
    if q.min_price is not None: df = df[df["price"] >= q.min_price]
    if q.max_price is not None: df = df[df["price"] <= q.max_price]
    if q.title_contains: df = df[df["title"].str.contains(q.title_contains, case=False, na=False)]
    
    # Сортировка
    df = df.sort_values(by=q.sort_by, ascending=(q.order == "asc"))
    
    # Пагинация
    df = df.iloc[q.offset : q.offset + q.limit]
    
    return df.rename(columns={"price": "price"}).to_dict(orient="records")

@router.get("/stats", response_model=StatsOut)
def get_stats():
    df = load_books()
    return {
        "total_books": len(df),
        "avg_price": round(df["price"].mean(), 2),
        "min_price": df["price"].min(),
        "max_price": df["price"].max(),
        "last_scraped": df["scraped_at"].max().isoformat()
    }