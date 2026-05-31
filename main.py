#!/usr/bin/env python3
import os
import sys
import pandas as pd
import numpy as np

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from scraper.collector import fetch_books
from scraper.storage import save_to_csv
from analysis.analyzer import load_and_clean
from analysis.visualize import plot_price_trend

# Путь к файлу артефактов (накапливаемые средние цены с шумом)
ARTIFACT_CSV = os.path.join(PROJECT_ROOT, "data", "reports", "price_trend_data.csv")
NOISE_FACTOR = 0.05  # ±5%

def process_latest_run(df_raw: pd.DataFrame) -> pd.DataFrame:

    df_raw['scraped_at'] = pd.to_datetime(df_raw['scraped_at'])
    latest_run = df_raw['scraped_at'].max()
    
    # Средняя цена только текущего запуска
    current_avg = df_raw[df_raw['scraped_at'] == latest_run]['price_num'].mean()
    
    # Контролируемый шум (уникальный, но воспроизводимый для каждого запуска)
    seed = int(pd.Timestamp(latest_run).timestamp()) % (2**32)
    np.random.seed(seed)
    noisy_avg = current_avg * np.random.uniform(1 - NOISE_FACTOR, 1 + NOISE_FACTOR)
    
    return pd.DataFrame([{
        'datetime': latest_run,
        'avg_price_noisy': round(noisy_avg, 2)
    }])

def main():
    print("Запуск скрапера...")
    
    # 1. Сбор и сохранение сырых данных с сайта
    raw_data = fetch_books()
    save_to_csv(raw_data)
    print("Сырые данные сохранены в data/raw/books_scraped.csv")
    
    # 2. Загрузка и очистка для анализа
    df = load_and_clean()
    
    # 3. Вычисление зашумлённого среднего для текущего запуска
    new_artifact_row = process_latest_run(df)
    
    # 4. Дозапись в отдельный .csv-артефакт
    os.makedirs(os.path.dirname(ARTIFACT_CSV), exist_ok=True)
    file_exists = os.path.exists(ARTIFACT_CSV)
    new_artifact_row.to_csv(ARTIFACT_CSV, mode='a', header=not file_exists, index=False)
    print(f"Артефакт обновлён: {ARTIFACT_CSV}")
    
    # 5. Построение графика по накопленным артефактам
    df_artifact = pd.read_csv(ARTIFACT_CSV, parse_dates=['datetime'])
    plot_price_trend(df_artifact)
    
    print("Готово! Файлы сохранены в data/")

if __name__ == "__main__":
    main()