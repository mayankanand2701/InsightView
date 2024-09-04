import streamlit as st

def sidebar_settings():
    st.sidebar.subheader("Upload Dataset")
    uploaded_file = st.sidebar.file_uploader("Choose a file", type="csv")
    return uploaded_file
