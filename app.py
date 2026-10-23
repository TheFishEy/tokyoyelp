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

    # Convert UI values to the values expected by recommender.py
    selected_cuisine = (
        "Anything" if cuisine == "Any" else cuisine
    )

    selected_neighborhood = (
        "Anywhere"
        if neighborhood == "Any"
        else neighborhood
    )

    results = recommend(
        restaurants,
        selected_neighborhood,
        selected_cuisine,
    )

    # Search filter
    if search.strip():
        ignored_words = {
            "near",
            "in",
            "at",
            "restaurant",
            "restaurants",
        }

        search_terms = [
            word.lower()
            for word in search.split()
            if word.lower() not in ignored_words
        ]

        results = [
            restaurant
            for restaurant in results
            if all(
                term in (
                    restaurant.get("name", "").lower()
                    + " "
                    + restaurant.get("genre", "").lower()
                    + " "
                    + restaurant.get("address", "").lower()
                    + " "
                    + restaurant.get("station", "").lower()
                    + " "
                    + restaurant.get("area", "").lower()
                )
                for term in search_terms
            )
        ]

    # Budget filter
    if budget != "Any":
        filtered_results = []

        for restaurant in results:
            dinner_budget = restaurant.get(
                "dinner_budget",
                "",
            )

            if budget == "¥":
                allowed = (
                    "999" in dinner_budget
                    or "1,999" in dinner_budget
                )

            elif budget == "¥¥":
                allowed = (
                    "2,000" in dinner_budget
                    or "2,999" in dinner_budget
                    or "3,000" in dinner_budget
                    or "3,999" in dinner_budget
                )

            else:
                allowed = (
                    "4,000" in dinner_budget
                    or "4,999" in dinner_budget
                    or "5,000" in dinner_budget
                    or "5,999" in dinner_budget
                    or "6,000" in dinner_budget
                )

            if allowed:
                filtered_results.append(restaurant)

        results = filtered_results

    if not results:
        st.info(
            "No restaurants found. Try changing your filters."
        )

    else:
        st.write(
            f"Showing {len(results)} restaurant(s)"
        )

        for restaurant in results[:20]:
            with st.container(border=True):
                st.subheader(restaurant["name"])

                st.write(
                    f"📍 {restaurant['address']}"
                )

                st.write(
                    f"🚉 Near {restaurant['station']} "
                    f"({restaurant['distance']} meters)"
                )

                st.write(
                    f"🍱 {restaurant['genre']}"
                )

                st.write(
                    f"⭐ Rating: {restaurant['rating']}"
                )

                st.write(
                    f"📝 Reviews: "
                    f"{restaurant['review_count']}"
                )

                st.write(
                    f"💴 Dinner budget: "
                    f"{restaurant['dinner_budget']}"
                )

except Exception as error:
    st.error(f"Unable to load restaurants: {error}")