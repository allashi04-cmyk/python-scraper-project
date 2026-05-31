# python-scraper-project

Непрерывный пайплайн сбора, накопления и анализа данных с `books.toscrape.com`.  
Проект демонстрирует архитектуру скрапинга, разделение сырых данных и артефактов анализа, а также визуализацию динамики цен во времени.

---


### Установка
```bash
git clone https://github.com/allashi04-cmyk/python-scraper-project.git
cd python-scraper-project

# Создание виртуального окружения
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Установка зависимостей
pip install -r requirements.txt
```
### Запуск скрапера
```bash
python main.py
```
### Важная информация
Чтобы увидеть линию тренда на графике, необходимо несколько раз запустить скрипер.
График расположен в /data/reports/price_trend.png

### Запуск Web-интерфейса
```bash
uvicorn api.main:app --reload --port 8000
```
API доступен по адресу: http://localhost:8000
Интерактивная документация (Swagger): http://localhost:8000/docs

|Метод|Путь|Описание|Параметры|
| ----------- | ----------- | ----------- | ----------- |
|GET|/books|срез данных|limit (1-50), offset, sort_by, order, min_price, max_price, title_contains|
|GET|/books/stats|статистика|- -|
|GET|/health|статус API|- -|

Примеры запросов
```bash
# 5 самых дешёвых книг
curl "http://localhost:8000/books?limit=5&sort_by=price&order=asc"

# Поиск по названию + фильтр цены
curl "http://localhost:8000/books?title_contains=python&min_price=20&limit=10"

# Статистика
curl "http://localhost:8000/books/stats"
```
