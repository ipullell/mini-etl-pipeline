import requests
import json
import time
from datetime import datetime


def extract():

    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
    time_stamp_file = datetime.now().strftime("%d%m%Y_%H%M%S")
    time_stamp_log = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    file_logs = "../logs/logs_ETL.txt"
    max_retries = 3

    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            file_name = f"../data/raw_crypto_{time_stamp_file}.json"
            file_logs = "../logs/logs_ETL.txt"

            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)

            with open(file_logs, "a") as file:
                file.write(f"{time_stamp_log} EXTRACT SUCCESSFULLY\n")

            return data

        except requests.exceptions.RequestException as e:
            with open(file_logs, "a") as file:
                file.write(f"{time_stamp_log} EXTRACT FAILED\n")

            if attempt == max_retries -1:
                raise RuntimeError(f"[STAGE EXTRACT] Failed to fetch data from Coingecko API. Detail: {e}")

        except ValueError as e:
            with open(file_logs, "a") as file:
                file.write(f"{time_stamp_log} EXTRACT FAILED\n")
            
            if attempt == max_retries -1:
                raise RuntimeError(f"[STAGE EXTRACT] API data format is not valid JSON. Detail: {e}")
        time.sleep(2)


if __name__ == "__main__":
    extract()