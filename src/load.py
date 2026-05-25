import os
import time
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine
from extract import extract
from transform import transform

load_dotenv()

def load(df):

    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    max_retries = 3
    time_stamp_file = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    time_stamp_log = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")


    for attempt in range(max_retries):
        try:
            engine = create_engine(
            f"postgresql://{user}:{password}@localhost:5432/crypto_db"
            )

            file_logs = "../logs/logs_ETL.txt"

            df.to_sql(
                "crypto_data",
                engine,
                if_exists = "replace",
                index = False
            )
            with open(file_logs, "a") as file:
                file.write(f"{time_stamp_log} LOAD SUCCESSFULLY\n")
            break

        except Exception as e:
            with open(file_logs, "a") as file:
                file.write(f"{time_stamp_file} LOAD FAILED\n")

            if attempt == max_retries -1:
                raise RuntimeError(f"[STAGE LOAD] Failed to save data to PostgreSQL. Detail: {e}")
        time.sleep(2)

if __name__ == "__main__":
    raw_data = extract()
    clean_data = transform(raw_data)
    load(clean_data)