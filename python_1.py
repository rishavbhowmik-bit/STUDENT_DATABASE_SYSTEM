import streamlit as st

st.title("Hello World")

name = st.text_input("Enter your name")

st.write("Welcome", name)