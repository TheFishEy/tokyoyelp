import streamlit as st

from data import get_restaurants
from recommender import recommend


st.set_page_config(
    page_title="Tokyo Restaurant Finder",
    page_icon="🍣",
)


st.title("🍣 Tokyo Restaurant Finder")

st.write(
    "Find Japanese restaurants in Tokyo using local Tabelog data."
)


area = st.selectbox(
    "Where do you want to eat?",
    [
        "Anywhere",
        "Chiyoda",
        "Shinjuku",
        "Shibuya",
        "Taito",
        "Minato",
        "Chuo",
    ],
)


cuisine = st.selectbox(
    "What are you craving?",
    [
        "Anything",
        "Sushi",
        "Ramen",
        "Yakiniku",
        "Izakaya",
        "Japanese",
    ],
)


if st.button("Find Restaurants"):
    try:
        with st.spinner("Loading restaurants..."):
            restaurants = get_restaurants()
            results = recommend(
                restaurants,
                area,
                cuisine,
            )

        if not results:
            st.warning("No restaurants found.")
        else:
            st.success(
                f"Found {len(results)} restaurant(s)."
            )

            for restaurant in results[:20]:
                st.subheader(restaurant["name"])

                st.write(
                    f"📍 **Address:** "
                    f"{restaurant['address']}"
                )

                st.write(
                    f"🚉 **Nearest station:** "
                    f"{restaurant['station']}"
                )

                st.write(
                    f"📏 **Distance:** "
                    f"{restaurant['distance']} meters"
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

                st.divider()

    except Exception as error:
        st.error(f"Unable to load restaurants: {error}")