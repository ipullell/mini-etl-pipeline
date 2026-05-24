import os
import time
from dotenv import load_dotenv
from sqlalchemy import create_engine
from extract import extract
from transform import transform

load_dotenv()

def load(df):

    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    try:
        engine = create_engine(
        f"postgresql://{user}:{password}@localhost:5432/crypto_db"
        )

        df.to_sql(
            "crypto_data",
            engine,
            if_exists = "replace",
            index = False
        )
        print("Data successfully saved to database.")
    except Exception as e:
        raise RuntimeError(f"[STAGE LOAD] Failed to save data to PostgreSQL. Detail: {e}")


if __name__ == "__main__":
    raw_data = extract()
    clean_data = transform(raw_data)
    print("\nSaving data to database...")
    time.sleep(2)
    load(clean_data)