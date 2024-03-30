import streamlit as st
import pandas as pd
import altair as alt
# import st.pyplot as plt

# Title of the app
st.title('Data Summarizing')

# Initialize df as an empty DataFrame
df = pd.DataFrame()

# Sidebar for navigation
option = st.sidebar.selectbox(
    'Choose your option',
    ('Data Visualisation', 'Analysis', 'Exit')
)

# Read CSV/Excel file
file = st.file_uploader("Upload a CSV", type=["csv"])
if file is not None:
    # Check if the file is a CSV or Excel file and read accordingly
    if file.type == "text/csv":
        df = pd.read_csv(file)
    # elif file.type == "xlsx":
    #     df = pd.read_excel(file)
    else:
        st.error("Unsupported file type. Please upload a CSV or Excel file.")
    
    # Display the file name and type
    st.write(f"File name: {file.name}")
    st.write(f"File type: {file.type}")
    st.write("File received successfully.")
    
    # Ask the user for the number of rows to display
    n = st.number_input('Enter the number of rows to display', min_value=1, max_value=len(df), value=5)
    st.write(df.head(n))

# The rest of your code for Data Visualisation, Analysis, and Manipulation sections remains the same
# Ensure to check if df is not empty before performing any operations on it


if option == 'Data Visualisation':
    # Visualization options
    visual_option = st.selectbox(
        'Choose a visualization type',
        ('Line Charts', 'Bar Charts', 'Horizontal Bar Charts', 'Scatter Charts')
    )

    # Allow the user to select columns for visualization
    x_column = st.selectbox('Select Variable 1', df.columns)
    y_column = st.selectbox('Select Variable 2', df.columns)

    if visual_option == 'Line Charts':
        st.subheader('Line Charts')
        st.line_chart(df[[x_column, y_column]])

    elif visual_option == 'Bar Charts':
        st.subheader('Bar Charts')
        st.bar_chart(df[[x_column, y_column]])

    elif visual_option == 'Horizontal Bar Charts':
        st.subheader('Horizontal Bar Charts')
        chart = alt.Chart(df).mark_bar().encode(
            x=y_column+':Q',
            y=x_column+':O'
        )
        st.altair_chart(chart, use_container_width=True)

    elif visual_option == 'Scatter Charts':
        st.subheader('Scatter Charts')
        st.scatter_chart(df[[x_column, y_column]])

   

elif option == 'Analysis':
    # Analysis options
    analysis_option = st.selectbox(
        'Choose an analysis type',
        ('Top records', 'Bottom records', 'Print particular column', 'Print multiple columns', 'Complete statistics', 'Information about dataframe', 'Unique values', 'Aggregate functions')
    )
    
    if analysis_option == 'Top records':
        n = st.number_input('Enter the number of records to display', min_value=1, max_value=len(df), value=5)
        st.write(df.head(n))
    
    elif analysis_option == 'Bottom records':
        n = st.number_input('Enter the number of records to display', min_value=1, max_value=len(df), value=5)
        st.write(df.tail(n))
    
    elif analysis_option == 'Print particular column':
        column_name = st.selectbox('Select a column', df.columns)
        st.write(df[column_name])
    
    elif analysis_option == 'Print multiple columns':
        columns_to_display = st.multiselect('Select columns to display', df.columns)
        st.write(df[columns_to_display])
    
    elif analysis_option == 'Complete statistics':
        st.write(df.describe())
    
    elif analysis_option == 'Information about dataframe':
        st.write(df.info())
    
    elif analysis_option == 'Unique values':
        column_name = st.selectbox('Select a column', df.columns)
        st.write(df[column_name].unique())
    
    elif analysis_option == 'Aggregate functions':
        column_name = st.selectbox('Select a column', df.columns)
        aggregation_function = st.selectbox('Select an aggregation function', ['mean', 'sum', 'min', 'max', 'count'])
        if aggregation_function == 'mean':
            st.write(df[column_name].mean())
        elif aggregation_function == 'sum':
            st.write(df[column_name].sum())
        elif aggregation_function == 'min':
            st.write(df[column_name].min())
        elif aggregation_function == 'max':
            st.write(df[column_name].max())
        elif aggregation_function == 'count':
            st.write(df[column_name].count())



elif option == 'Exit':
    st.write('Exiting the application.')

# Check if the logout button was pressed


st.page_link("https://nimble-custard-c705a0.netlify.app/", label="LogOut", icon="🏠")