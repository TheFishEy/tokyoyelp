import streamlit as st
from data import get_restaurants
from recommender import recommend

st.title("TokyoYelp")
st.write("Are you unsure of what restraunts you'll like on your next weeb trip?")
st.write("Have no fear! Get recommended OUSHI tokyo restaruants!")


# User preferences
area = st.selectbox(
    "Where do you want to eat?",
    ["Anywhere", "Shinjuku", "Shibuya", "Asakusa"]
)

cuisine = st.selectbox(
    "What are you craving?",
    ["Anything", "Ramen", "Sushi", "Yakiniku"]
)

if st.button("Find Restaurants"):
    st.write(f"Searching for {cuisine} in {area}...")
