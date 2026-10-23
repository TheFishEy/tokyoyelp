import streamlit as st

st.set_page_config(
    page_title="Tokyo Table",
    # page_icon="",
    layout="wide"
)

st.title("Tokyo Table")
st.write("Find your next favorite restaurant in Tokyo.")

search = st.text_input(
    "What are you looking for?",
    placeholder="Try: sushi near Shibuya"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.selectbox("Cuisine", ["Any", "Ramen", "Sushi", "Izakaya"])

with col2:
    st.selectbox("Neighborhood", ["Any", "Shibuya", "Shinjuku", "Ginza"])

with col3:
    st.selectbox("Budget", ["Any", "¥", "¥¥", "¥¥¥"])

st.subheader("Recommended restaurants")

st.info("Your restaurant recommendations will appear here.")