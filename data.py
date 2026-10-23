from pathlib import Path

import pandas as pd
import streamlit as st


DATASET_PATH = (
    Path(__file__).parent
    / "data"
    / "Tokyo_Restaurant_Reviews_Tabelog.csv"
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
            "id": str(row["store_id"]),
            "name": str(row["name"]).strip(),
            "station": str(row["nearest_station"]).strip(),
            "distance": str(row["nearest_distance"]).strip(),
            "genre": str(row["genre"]).strip(),
            "rating": float(row["rating_val"] or 0),
            "review_count": int(float(row["review_cnt"] or 0)),
            "dinner_budget": str(row["budget_dinner"]).strip(),
            "lunch_budget": str(row["budget_lunch"]).strip(),
            "address": str(row["address"]).strip(),
            "area": str(row["municipalities_1"]).strip(),
        })

    return restaurants