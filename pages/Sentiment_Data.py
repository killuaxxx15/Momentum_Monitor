import pandas as pd
import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title='Sentiment Data', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('Sentiment Data')

# Display the last update date
st.markdown('#### Updated: 24/05/2024')

# Define Excel file and sheet name variables
excel_file = 'Sentiment_Data_24_05_2024.xlsx'
sheet_name = 'Sheet1'

# Cache data loading function for better performance
@st.cache
def load_excel_data(file_name, sheet, use_columns, header_row, num_rows):
    return pd.read_excel(file_name, sheet_name=sheet, usecols=use_columns, header=header_row, nrows=num_rows)

# TABLE 1
df1 = load_excel_data(excel_file, sheet_name, 'F:K', 10, 5)
df1 = df1.fillna('')
# Format specific cells as percentages
df1.iloc[1:3, 2] = df1.iloc[1:3, 2].apply(lambda x: f'{x:.2%}')
df1.iloc[4:5, 2] = df1.iloc[4:5, 2].apply(lambda x: f'{x:.2%}')
#df1.iloc[1:3, 3] = df1.iloc[1:3, 3].apply(lambda x: f'{x:.0%}')
#df1.iloc[4:5, 3] = df1.iloc[4:5, 3].apply(lambda x: f'{x:.0%}')
st.dataframe(df1, hide_index=True)
st.markdown(' ### ')

# TABLE 2
df2 = load_excel_data(excel_file, sheet_name, 'F:K', 19, 1)
df2 = df2.fillna('')
st.dataframe(df2, hide_index=True)

st.header('Bull/Bear Ratios')
st.image('fig1_24_05_2024.png', caption='Figure 1', use_column_width=True)

st.header('Put/Call & Vix')
st.image('fig2_24_05_2024.png', caption='Figure 2', use_column_width=True)

st.image('fig33.jpeg', caption='Figure 3', use_column_width=True)
