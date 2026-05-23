import requests
import sys
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
        file_name = f"../data/raw_btc_{timestamp}.json"

        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Successfully saved Raw Data to {file_name}")

        return data

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch API data. Error:  {e}")
        sys.exit(1)

    except ValueError:
        print("API response is not valid JSON")
        sys.exit(1)


if __name__ == "__main__":
    print("Fetching API data...")
    time.sleep(2)
    print("Saving raw data to JSON file...")
    extract()