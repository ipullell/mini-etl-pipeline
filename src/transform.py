import pandas as pd
import json

data_clean = []

def transform(data):

    data_clean.clear()


    for raw in data:
        clean = {
            "id" : raw["id"],
            "name" : raw["name"],
            "current_price" : raw["current_price"],
            "market_cap" : raw["market_cap"],
            "total_volume" : raw["total_volume"],
            "last_updated" : raw["last_updated"],
        }
        data_clean.append(clean)

    