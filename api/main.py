from fastapi import FastAPI
from api.router import books

app = FastAPI(
    title="Book Scraper API",
    description="Интерфейс для работы с данными проекта скрапинга",
    version="1.0.0"
)

# 👇 Приветственная страница
@app.get("/")
def root():
    return {
        "message": "Book Scraper API работает",
        "docs": "/docs",
        "redoc": "/redoc",
        "endpoints": ["/books", "/books/stats", "/health"]
    }

app.include_router(books.router)

@app.get("/health")
def health():
    return {"status": "ok", "message": "API и данные готовы к работе"}