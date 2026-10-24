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
    ).fillna("")

    restaurants = []

    for _, row in dataframe.iterrows():
        restaurants.append(
            {
                "id": str(
                    row["restaurant_id"]
                ).strip(),

                "name": str(
                    row["name"]
                ).strip(),

                "station": str(
                    row["nearest_station"]
                ).strip(),

                "distance": to_float(
                    row["distance_from_station_m"]
                ),

                "genre": str(
                    row["cuisine"]
                ).strip(),

                "rating": to_float(
                    row["rating"]
                ),

                "review_count": to_int(
                    row["review_count"]
                ),

                "dinner_budget": str(
                    row["dinner_price"]
                ).strip(),

                "lunch_budget": str(
                    row["lunch_price"]
                ).strip(),

                "address": str(
                    row["address"]
                ).strip(),

                "area": (
                    str(row["city"]).strip()
                    + " "
                    + str(row["district"]).strip()
                    + " "
                    + str(row["area"]).strip()
                ),
            }
        )

    return restaurants


def to_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def to_int(value):
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return 0