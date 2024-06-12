import pandas as pd
import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title='Commodities', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('Commodities (waiting for data)')

# Display the last update date
st.markdown('#### Updated: 12/06/2024')

# Define Excel file and sheet name variables
excel_file = 'COMMODITIES_MOMENTUM_RANKINGS_10_06_2024.xlsx'
sheet_name = 'Aset class Rankings'

# Cache data loading function for better performance
@st.cache
def load_excel_data(file_name, sheet, use_columns, header_row, num_rows):
    return pd.read_excel(file_name, sheet_name=sheet, usecols=use_columns, header=header_row, nrows=num_rows)

# Function to apply background color based on cell value
def color_cells(val):
    color = '#ffcccc' if val == 'CASH' else ('#ccffcc' if val == 'INVESTED' else '')
    return f'background-color: {color}'


# TABLE 1
df1 = load_excel_data(excel_file, sheet_name, 'D:K', 5, 14)
df1 = df1.rename(columns={'Unnamed: 3' : 'Code'})
df1 = df1.rename(columns={'Unnamed: 4' : 'Commodity'})
df1 = df1.rename(columns={'Above 30 D ' : 'Current Ranking.1'})
df1 = df1.rename(columns={'Above 60 D' : 'Above 30 D '})
df1 = df1.rename(columns={'Above 200D' : 'Above 60 D'})
df1 = df1.rename(columns={'Unnamed: 10' : 'Above 200D'})
df1 = df1.style.applymap(color_cells, subset=['Above 30 D ', 'Above 60 D', 'Above 200D'])
st.markdown('### Relative Ranking')
st.dataframe(df1, hide_index=True)




