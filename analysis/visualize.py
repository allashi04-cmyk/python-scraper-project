import os
import matplotlib
matplotlib.use('Agg')  #  Важно: отключает GUI-окна в облачной среде
import matplotlib.pyplot as plt
import pandas as pd

def plot_price_trend(df: pd.DataFrame):
    daily_avg = df.groupby(df["scraped_at"].dt.date)["price_num"].mean().reset_index()
    daily_avg.columns = ["date", "avg_price"]

    plt.figure(figsize=(8, 5))
    plt.plot(daily_avg["date"], daily_avg["avg_price"], marker="o", linestyle="-", color="#1f77b4")
    plt.title("Динамика средней цены книг")
    plt.xlabel("Дата запуска")
    plt.ylabel("Средняя цена (£)")
    plt.grid(alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()

    reports_dir = os.path.join(os.path.dirname(__file__), "..", "data", "reports")
    os.makedirs(reports_dir, exist_ok=True)
    path = os.path.join(reports_dir, "price_trend.png")
    plt.savefig(path, dpi=150)
    print(f" График сохранён: {path}")
