import streamlit as st
import re

from data import get_restaurants
from recommender import recommend


st.set_page_config(
    page_title="Tokyo Table",
    layout="wide",
)


st.title("Tokyo Table")
st.write("Find your next favorite restaurant in Tokyo.")


search = st.text_input(
    "What are you looking for?",
    placeholder="Try: sushi near Shibuya",
)



col1, col2, col3, col4 = st.columns(4)

with col1:
    cuisine = st.selectbox(
        "Cuisine",
        ["Any", "Ramen", "Sushi", "Izakaya"],
    )

## neighborhood dropdown
with col2:
    neighborhood = st.selectbox(
        "Neighborhood",
        ["Any", "Shibuya", "Shinjuku", "Ginza"],
    )

## budget dopdown
with col3:
    budget = st.selectbox(
        "Budget (¥1,000=$6)",
        ["Any", "¥", "¥¥", "¥¥¥", "¥¥¥¥", "¥¥¥¥¥"],
    )

with col4:
    rating = st.selectbox(
        "Tabelog Rating",
        ["Any", "⭐ (>2.4)", "⭐⭐ (>2.7)", "⭐⭐⭐ (>3)", "⭐⭐⭐⭐ (>3.3)", "⭐⭐⭐⭐⭐ (3.5)"],
    )

st.subheader("Recommended restaurants")


try:
    restaurants = get_restaurants()

    # Match the UI values with recommender.py values
    cuisine_filter = (
        "Anything"
        if cuisine == "Any"
        else cuisine
    )

    neighborhood_filter = {
        "Any": "Anywhere",
        "Shibuya": "Shibuya",
        "Shinjuku": "Shinjuku",
        "Ginza": "Chuo",
    }[neighborhood]

    results = recommend(
        restaurants,
        neighborhood_filter,
        cuisine_filter,
        rating=rating,
    )

    # Search filter
    if search.strip():
        search_map = {
            "sushi": ["寿司", "鮨", "すし"],
            "ramen": ["ラーメン", "らーめん", "つけ麺"],
            "izakaya": ["居酒屋"],
            "shibuya": ["渋谷区"],
            "shinjuku": ["新宿区"],
            "ginza": ["中央区", "銀座"],
        }

        ignored_words = {
            "near",
            "in",
            "at",
            "restaurant",
            "restaurants",
        }

        search_words = [
            word.lower()
            for word in search.split()
            if word.lower() not in ignored_words
        ]

        filtered_results = []

        for restaurant in results:
            searchable_text = (
                restaurant.get("name", "")
                + " "
                + restaurant.get("genre", "")
                + " "
                + restaurant.get("address", "")
                + " "
                + restaurant.get("station", "")
                + " "
                + restaurant.get("area", "")
            ).lower()

            matches_all_words = True

            for word in search_words:
                translated_words = search_map.get(
                    word,
                    [word],
                )

                matches_word = any(
                    translated_word.lower()
                    in searchable_text
                    for translated_word in translated_words
                )

                if not matches_word:
                    matches_all_words = False
                    break

            if matches_all_words:
                filtered_results.append(restaurant)

        results = filtered_results


    # Budget filter
    if budget != "Any":
        filtered = []

        for r in results:
            price = re.search(
                r"\d[\d,]*", str(r["dinner_budget"])
            )

            if not price:
                continue

            yen = int(price.group().replace(",", ""))
            tier = min(yen // 3000 + 1, 5) # never excede 5

            if budget == "¥" * tier:
                filtered.append(r)

        results = filtered

    if not results:
        st.info(
            "No restaurants found. "
            "Try changing your search or filters."
        )
    else:
        st.write(
            f"Showing {len(results)} restaurant(s)"
        )

        for restaurant in results[:20]:
            with st.container(border=True):
                st.subheader(restaurant["name"])

                st.write(
                    f"📍 **Address:** "
                    f"{restaurant['address']}"
                )

                st.write(
                    f"🚉 **Nearest station:** "
                    f"{restaurant['station']} "
                    f"({restaurant['distance']} meters)"
                )

                st.write(
                    f"🍱 **Genre:** "
                    f"{restaurant['genre']}"
                )

                st.write(
                    f"⭐ **Rating:** "
                    f"{restaurant['rating']}"
                )

                st.write(
                    f"📝 **Reviews:** "
                    f"{restaurant['review_count']}"
                )

                st.write(
                    f"💴 **Dinner budget:** "
                    f"{restaurant['dinner_budget']}"
                )

except Exception as error:
    st.error(f"Unable to load restaurants: {error}")