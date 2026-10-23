import streamlit as st

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


col1, col2, col3 = st.columns(3)


with col1:
    cuisine = st.selectbox(
        "Cuisine",
        ["Any", "Ramen", "Sushi", "Izakaya"],
    )


with col2:
    neighborhood = st.selectbox(
        "Neighborhood",
        ["Any", "Shibuya", "Shinjuku", "Ginza"],
    )


with col3:
    budget = st.selectbox(
        "Budget",
        ["Any", "¥", "¥¥", "¥¥¥"],
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
        budget_results = []

        for restaurant in results:
            dinner_budget = restaurant.get(
                "dinner_budget",
                "",
            )

            if budget == "¥":
                matches_budget = (
                    "999" in dinner_budget
                    or "1,999" in dinner_budget
                )

            elif budget == "¥¥":
                matches_budget = (
                    "2,000" in dinner_budget
                    or "2,999" in dinner_budget
                    or "3,000" in dinner_budget
                    or "3,999" in dinner_budget
                )

            else:
                matches_budget = (
                    "4,000" in dinner_budget
                    or "4,999" in dinner_budget
                    or "5,000" in dinner_budget
                    or "5,999" in dinner_budget
                    or "6,000" in dinner_budget
                )

            if matches_budget:
                budget_results.append(restaurant)

        results = budget_results

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