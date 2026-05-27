import streamlit as st
from agent import generate_trip_plan

st.set_page_config(page_title="AI Travel Planner", layout="wide")

st.title("✈️ Agentic AI Travel Planning Assistant")

source = st.text_input("Source City")
destination = st.text_input("Destination City")

days = st.slider("Number of Days", 1, 7, 3)

budget = st.number_input("Budget (₹)", min_value=1000)

interests = st.multiselect(
    "Travel Interests",
    ["Beach", "Adventure", "Historical", "Nature", "Food", "Shopping"]
)

if st.button("Generate Trip Plan"):

    user_data = {
        "source": source,
        "destination": destination,
        "days": days,
        "budget": budget,
        "interests": interests
    }

    result = generate_trip_plan(user_data)

    st.subheader("📌 Trip Summary")
    st.write(result)