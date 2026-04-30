import os
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
CSV_PATH = os.path.join(DATA_DIR, "books_scraped.csv")

def save_to_csv(data: list[dict]):
    os.makedirs(DATA_DIR, exist_ok=True)
    df = pd.DataFrame(data)
    
    if os.path.exists(CSV_PATH):
        old = pd.read_csv(CSV_PATH)
        df = pd.concat([old, df], ignore_index=True)
    
    df.to_csv(CSV_PATH, index=False)
    print(f" Данные сохранены в {CSV_PATH} (всего записей: {len(df)})")