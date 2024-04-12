import pandas as pd
import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title='Sentiment Data', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('Sentiment Data to be updated')

# Define Excel file and sheet name variables
excel_file = 'Sentimnet data.xlsx'
sheet_name = 'Sheet1'

# Cache data loading function for better performance
@st.cache
def load_excel_data(file_name, sheet, use_columns, header_row, num_rows):
    return pd.read_excel(file_name, sheet_name=sheet, usecols=use_columns, header=header_row, nrows=num_rows)

# TABLE 1
df1 = load_excel_data(excel_file, sheet_name, 'F:K', 10, 5)
df1 = df1.fillna('')
st.dataframe(df1, hide_index=True)
st.markdown(' ### ')

# TABLE 2
df2 = load_excel_data(excel_file, sheet_name, 'F:K', 19, 1)
df2 = df2.fillna('')
st.dataframe(df2, hide_index=True)
st.markdown(' ### ')

