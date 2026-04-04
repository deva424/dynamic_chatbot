import schedule
import time
from src.ingestion.processor import update_vector_database

# List of dynamic sources to monitor
SOURCES = [
    "https://example.com/latest-news",
    "https://api.yourservice.com/docs"
]

def job():
    print("Syncing knowledge base...")
    update_vector_database(SOURCES)

# Schedule to run every hour
schedule.every().hour.do(job)

if __name__ == "__main__":
    # Run once on startup, then keep running
    job() 
    while True:
        schedule.run_pending()
        time.sleep(60)