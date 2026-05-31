import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

def plot_price_trend(df: pd.DataFrame):
    """Строит график по накопленным артефактам (datetime, avg_price_noisy)."""
    plt.figure(figsize=(10, 6))
    plt.plot(df['datetime'], df['avg_price_noisy'], 
             marker='o', linestyle='-', color='#1f77b4', linewidth=2)
    
    plt.title('Динамика средней цены книг по запускам')
    plt.xlabel('Время запуска')
    plt.ylabel('Средняя цена (£)')
    plt.grid(alpha=0.3, linestyle='--')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    reports_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'reports')
    os.makedirs(reports_dir, exist_ok=True)
    path = os.path.join(reports_dir, 'price_trend.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"График сохранён: {path}")
    print(f"Точек на графике: {len(df)}")