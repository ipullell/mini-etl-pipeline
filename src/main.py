import time

from extract import extract
from transform import transform
from load import load


def main():

    print("=== STARTING ETL PROCESS ===")

    try:
        print("\nFetching API data...")
        time.sleep(2)

        raw_data = extract()


        print("\nTransforming raw data...")
        time.sleep(2)

        clean_data = transform(raw_data)


        print("\nLoading data to PostgreSQL...")
        time.sleep(2)

        load(clean_data)


        print("\n=== ETL PROCESS COMPLETED SUCCESSFULLY ===")

    except Exception as e:
        print(f"\n[CRITICAL ERROR] {e}")



if __name__ == "__main__":
    main()