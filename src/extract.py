import requests
import json
import time
from datetime import datetime


def extract():

    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()


        timestamp = datetime.now().strftime("%d-%m-%Y")
        file_name = f"../data/raw_crypto_{timestamp}.json"

        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Successfully saved Raw Data to {file_name}")

        return data

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"[STAGE EXTRACT] Failed to fetch data from Coingecko API. Detail: {e}")

    except ValueError as e:
        raise RuntimeError(f"[STAGE EXTRACT] Format data dari API bukan JSON yang valid. Detail: {e}")


if __name__ == "__main__":
    print("Fetching API data...")
    time.sleep(2)
    print("Saving raw data to JSON file...")
    extract()