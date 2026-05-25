import pandas as pd
from datetime import datetime
from extract import extract

def transform(data):

    try:
        df = pd.DataFrame(data)
        time_stamp_log = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        file_logs = "../logs/logs_ETL.txt"

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

        with open(file_logs, "a") as file:
            file.write(f"{time_stamp_log} TRANSFORM SUCCESSFULLY\n")

        return df

    except KeyError as e:
        with open(file_logs, "a") as file:
            file.write(f"{time_stamp_log} TRANSFORM FAILED\n")
        raise RuntimeError(f"[STAGE TRANSFORM] Column {e} not found in the raw API data!")


if __name__ == "__main__":
    raw_data = extract()
    clean_data = transform(raw_data)
    print(clean_data.head(6))