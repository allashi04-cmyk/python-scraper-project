from prefect import flow, task
from prefect.schedules import CronSchedule
from scraper.collector import fetch_books
from scraper.storage import save_to_csv
from analysis.analyzer import load_and_clean, get_insights
from analysis.visualize import plot_price_trend

@task
def run_scraper():
    return fetch_books()

@task
def save_data(data):
    save_to_csv(data)

@task
def run_analysis():
    df = load_and_clean()
    insights = get_insights(df)
    print(" Инсайты:", insights)
    plot_price_trend(df)

@flow(
    name="books-monitoring-flow",
    log_prints=True,
    schedule=CronSchedule(cron="0 12 * * *", timezone="UTC")  # Каждый день в 12:00 UTC
)
def monitoring_flow():
    data = run_scraper()
    save_data(data)
    run_analysis()

if __name__ == "__main__":
    # Запуск вручную для теста
    monitoring_flow()