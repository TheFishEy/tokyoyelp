
import streamlit as st

st.title("TokyoYelp")
st.write("Get recommended OUSHI tokyo restaruants (OUSHI!)")

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
