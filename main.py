#!/usr/bin/env python3
import os
import sys

#  Гарантируем, что Python видит пакеты проекта
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Теперь импорты сработают
from scraper.collector import fetch_books
from scraper.storage import save_to_csv
from analysis.analyzer import load_and_clean, get_insights
from analysis.visualize import plot_price_trend

def main():
    print(" Запуск скрапера...")
    data = fetch_books()
    save_to_csv(data)
    
    print(" Запуск анализа...")
    df = load_and_clean()
    print(" Инсайты:", get_insights(df))
    plot_price_trend(df)
    print(" Готово! Файлы сохранены в data/")

if __name__ == "__main__":
    main()