import time
from app.monitor import save_metrics

if __name__ == "__main__":
    while True:
        save_metrics()
        time.sleep(5)  # every 5 seconds
