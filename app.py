import streamlit as st
from utils.data_loader import load_data
from resources.sidebar import sidebar_settings
from resources.main_view import display_main_view

st.title("InsightView : Data Visualization Tool")

# Sidebar settings
uploaded_file = sidebar_settings()

# Main view
if uploaded_file is not None:
    df = load_data(uploaded_file)
    display_main_view(df)

