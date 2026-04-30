import pandas as pd
import os

RAW_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "books_scraped.csv")

def load_and_clean() -> pd.DataFrame:
    if not os.path.exists(RAW_PATH):
        raise FileNotFoundError("Нет сырых данных. Запустите скрапер сначала.")
    
    df = pd.read_csv(RAW_PATH)
    df["scraped_at"] = pd.to_datetime(df["scraped_at"])
    
    def clean_price(price_str):
        if pd.isna(price_str):
            return 0.0
        cleaned = ''.join(c for c in str(price_str) if c.isdigit() or c == '.')
        return float(cleaned) if cleaned else 0.0
    
    df["price_num"] = df["price"].apply(clean_price)
    return df

def get_insights(df: pd.DataFrame) -> dict:
    total_books = len(df)
    avg_price = df["price_num"].mean()
    latest_run = df["scraped_at"].max()
    runs_count = df["scraped_at"].nunique()
    
    return {
        "total_records": total_books,
        "avg_price_gbp": round(avg_price, 2),
        "scraping_runs": runs_count,
        "last_updated": latest_run.isoformat()
    }