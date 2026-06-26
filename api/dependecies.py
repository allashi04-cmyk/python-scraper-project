import pandas as pd
import os
from pathlib import Path
from fastapi import HTTPException

PROJECT_ROOT = Path(__file__).parent.parent
CSV_PATH = PROJECT_ROOT / "data" / "raw" / "books_scraped.csv"

def load_books() -> pd.DataFrame:
    if not CSV_PATH.exists():
        raise HTTPException(404, "Файл с данными не найден. Сначала запустите scraper.")
    df = pd.read_csv(CSV_PATH)
    df['scraped_at'] = pd.to_datetime(df['scraped_at'])

    if 'price' in df.columns:
        df['price'] = (
            df['price']
            .astype(str)
            .str.replace('£', '', regex=False)
            .str.replace('Â', '', regex=False)
            .str.replace('$', '', regex=False)
            .str.replace('€', '', regex=False)
            .str.strip()
        )
        # Конвертируем в numeric
        df['price'] = pd.to_numeric(df['price'], errors='coerce')

    # Оставляем только уникальные записи по последней метке времени (опционально)
    return df.dropna(subset=["price", "title"])