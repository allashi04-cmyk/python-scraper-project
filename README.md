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
