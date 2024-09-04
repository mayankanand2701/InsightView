import streamlit as st
from utils.visualizations import create_plot
import io

def display_main_view(df):
    # Convert entire DataFrame to strings to avoid conversion issues
    df_str = df.astype(str)

    st.sidebar.header("EDA Options")
    
    # Checkboxes for various EDA operations
    show_first_5_rows = st.sidebar.checkbox("Show First 5 Rows")
    show_last_5_rows = st.sidebar.checkbox("Show Last 5 Rows")
    show_column_names = st.sidebar.checkbox("Show Column Names")
    show_data_types = st.sidebar.checkbox("Show Data Types")
    show_shape = st.sidebar.checkbox("Show DataFrame Shape")
    show_summary = st.sidebar.checkbox("Show Summary Statistics")
    show_missing_data = st.sidebar.checkbox("Show Missing Data Count")
    show_data_info = st.sidebar.checkbox("Show DataFrame Info")
    show_unique_values = st.sidebar.checkbox("Show Unique Values Count")
    show_value_counts = st.sidebar.checkbox("Show Value Counts for Categorical Columns")
    show_correlation_matrix = st.sidebar.checkbox("Show Correlation Matrix")
    show_duplicate_rows = st.sidebar.checkbox("Show Duplicate Rows")

    # Perform EDA operations based on selected options
    if show_first_5_rows:
        st.subheader("First 5 Rows of Data")
        st.write(df_str.head())
    
    if show_last_5_rows:
        st.subheader("Last 5 Rows of Data")
        st.write(df_str.tail())
    
    if show_column_names:
        st.subheader("Column Names")
        st.write(df.columns.tolist())
    
    if show_data_types:
        st.subheader("Data Types of Columns")
        for column, dtype in df_str.dtypes.items():
            st.text(f"{column}: {dtype}")
    
    if show_shape:
        st.subheader("Shape of the DataFrame")
        st.write(df.shape)

    if show_summary:
        st.subheader("Summary Statistics")
        st.write(df.describe())
    
    if show_missing_data:
        st.subheader("Missing Data Count for Each Column")
        for column, missing in df.isnull().sum().items():
            st.text(f"{column}: {missing}")
    
    if show_data_info:
        st.subheader("DataFrame Info")
        buffer = io.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
    
    if show_unique_values:
        st.subheader("Unique Values Count for Each Column")
        for column in df.columns:
            st.text(f"{column}: {df[column].nunique()}")

    if show_value_counts:
        st.subheader("Value Counts for Categorical Columns")
        categorical_columns = df.select_dtypes(include=['object']).columns
        for column in categorical_columns:
            st.text(f"{column} Value Counts:")
            st.write(df[column].value_counts())

    if show_correlation_matrix:
        st.subheader("Correlation Matrix")
        st.write(df.corr())

    if show_duplicate_rows:
        st.subheader("Duplicate Rows in DataFrame")
        duplicates = df[df.duplicated()]
        if duplicates.empty:
            st.write("No duplicate rows found in the DataFrame.")
        else:
            st.write(duplicates)

    st.sidebar.header("Visualization Options")
    
    # Select X and Y columns for plotting
    x_column = st.sidebar.selectbox("Select X-axis", df.columns)
    y_column = st.sidebar.selectbox("Select Y-axis", df.columns)

    # Select the type of plot
    plot_type = st.sidebar.selectbox("Select Visualization Type", ["Line", "Bar", "Histogram", "Pie", "Density"])
    
    # Generate plot based on selected type
    if st.sidebar.button("Generate Plot"):
        if plot_type=="Line":st.subheader("Line Chart")
        elif plot_type=="Bar":st.subheader("Bar Chart")
        elif plot_type=="Histogram":st.subheader("Histogram")
        elif plot_type=="Pie":st.subheader("Pie")
        elif plot_type=="Density":st.subheader("Density Plot")
        fig = create_plot(df, x_column, y_column, plot_type)
        st.plotly_chart(fig) 

