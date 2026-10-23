from pathlib import Path

import pandas as pd
import streamlit as st


DATASET_PATH = (
    Path(__file__).parent
    / "data"
    / "restaurants_english_final.csv"
)


@st.cache_data
def get_restaurants():
    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found at: {DATASET_PATH}"
        )

    dataframe = pd.read_csv(
        DATASET_PATH,
        encoding="utf-8-sig",
    )

    dataframe = dataframe.fillna("")

    restaurants = []

    for _, row in dataframe.iterrows():
        restaurants.append({
            "id": str(row["restaurant_id"]),
            "name": str(row["name"]).strip(),
            "station": str(row["nearest_station"]).strip(),
            "distance": str(
                row["distance_from_station_m"]
            ).strip(),
            "genre": str(row["cuisine"]).strip(),
            "rating": float(row["rating"] or 0),
            "review_count": int(
                float(row["review_count"] or 0)
            ),
            "dinner_budget": str(
                row["dinner_price"]
            ).strip(),
            "lunch_budget": str(
                row["lunch_price"]
            ).strip(),
            "address": str(row["address"]).strip(),
            "area": (
                str(row["city"]).strip()
                + " "
                + str(row["district"]).strip()
                + " "
                + str(row["area"]).strip()
            ),
        })

    return restaurants