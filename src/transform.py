import pandas as pd
import time
from extract import extract

def transform(data):

    try:
        df = pd.DataFrame(data)

        df = df[
            [
                "id",
                "name",
                "current_price",
                "market_cap",
                "total_volume",
                "last_updated"
            ]
        ]

        return df

    except KeyError as e:
        raise RuntimeError(f"[STAGE TRANSFORM] Column {e} not found in the raw API data!")


if __name__ == "__main__":
    raw_data = extract()
    clean_data = transform(raw_data)
    print("\nRaw Data Filtering Process...")
    time.sleep(2)
    print("-" * 100)
    print(clean_data.head(6))
    print("-" * 100)
    print("Data successfully filtered.")