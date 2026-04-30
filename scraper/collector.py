import logging
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def fetch_books(url: str = "https://books.toscrape.com/") -> list[dict]:
    logging.info(f" Запуск скрапера: {url}")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        html = response.text
    except requests.RequestException as e:
        logging.error(f" Ошибка запроса: {e}")
        return []

    soup = BeautifulSoup(html, "html.parser")
    books = []
    timestamp = datetime.now().isoformat()

    for product in soup.select("article.product_pod"):
        title = product.h3.a.get("title") if product.h3.a else "Unknown"
        price_el = product.select_one("p.price_color")
        price = price_el.text.strip() if price_el else "N/A"
        rating_el = product.select_one("p.star-rating")
        rating = rating_el.get("class")[1] if rating_el and rating_el.get("class") else "Unknown"
        link = url + product.h3.a.get("href") if product.h3.a else url
        
        books.append({
            "scraped_at": timestamp,
            "title": title,
            "price": price,
            "rating": rating,
            "url": link
        })

    logging.info(f" Собрано {len(books)} записей")
    return books