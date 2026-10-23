
import pandas as pd
from pathlib import Path
from functools import lru_cache

@lru_cache(maxsize=1)
def get_restaurants():
    path = Path(__file__).with_name("restaurants.csv")
    df = pd.read_csv(path)

    # Keep Tokyo restaurants
    df = df[df["prefecture"] == "東京"].copy()

    # Clean missing values
    df["rating_val"] = pd.to_numeric(
        df["rating_val"], errors="coerce"
    ).fillna(0)

    df["review_cnt"] = pd.to_numeric(
        df["review_cnt"], errors="coerce"
    ).fillna(0)

    df = df.fillna("")

    # Convert CSV columns to our application's format
    restaurants = []

    for _, row in df.iterrows():
        restaurants.append({
            "name": row["name"],
            "area": row["municipalities_1"],
            "neighborhood": row["municipalities_2"],
            "station": row["nearest_station"],
            "cuisine": row["genre"],
            "rating": float(row["rating_val"]),
            "reviews": int(row["review_cnt"]),
            "description": (
                f"Rating: {row['rating_val']} | "
                f"Reviews: {int(row['review_cnt'])} | "
                f"Dinner: {row['budget_dinner']}"
            )
        })

    return restaurants
