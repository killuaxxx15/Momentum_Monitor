import pandas as pd
import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title='ETF Model DEVELOPED', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('ETF Model DEVELOPED')

# Display the last update date
st.markdown('#### Updated: 15/03/2024')

# Define Excel file and sheet name variables
excel_file = 'ETF_Model_DEVELOPED_22_03_2024.xlsx'
sheet_name1 = 'OUTPUT_COUNTRY'
sheet_name2 = 'OUTPUT_PPT'

# Cache data loading function for better performance
@st.cache
def load_excel_data(file_name, sheet, use_columns, header_row, num_rows):
    return pd.read_excel(file_name, sheet_name=sheet, usecols=use_columns, header=header_row, nrows=num_rows)

# Format percentage as whole number
def percent_whole_number(val):
    return "{:.0f}%".format(val * 100)


# TABLE 1
df1 = load_excel_data(excel_file, sheet_name1, 'B:N', 4, 13)
df1 = df1.drop(['Unnamed: 6'], axis=1)
df1 = df1.rename(columns={'Unnamed: 1' : 'TICKER'})
df1 = df1.rename(columns={'Unnamed: 2' : 'ETF'})
df1 = df1.rename(columns={'VALUE' : 'COM - VALUE'})
df1 = df1.rename(columns={'QUALITY' : 'COM - QUALITY'})
df1 = df1.rename(columns={'SAFETY' : 'COM - SAFETY'})
df1 = df1.rename(columns={'Unnamed: 7' : 'COMPOSITE VALUE SCORE'})
df1 = df1.rename(columns={'Unnamed: 8' : 'LIQUIDITY'})
df1 = df1.rename(columns={'SCORE' : 'MOM - SCORE'})
df1 = df1.rename(columns={'UPGRADES' : 'MOM - UPGRADES'})
df1 = df1.rename(columns={'Unnamed: 11' : 'CURRENCY'})
df1 = df1.rename(columns={'Unnamed: 12' : 'OVERALL SCORE'})
df1 = df1.rename(columns={'Unnamed: 13' : 'OVERALL RANK'})

df1 = df1.style.format({
    'COM - VALUE': '{:.1f}',
    'COM - QUALITY': '{:.1f}',
    'COM - SAFETY': '{:.1f}',
    'COMPOSITE VALUE SCORE': '{:.1f}',
    'LIQUIDITY': '{:.1f}',
    'MOM - SCORE': '{:.1f}',
    'MOM - UPGRADES': percent_whole_number,
    'CURRENCY': '{:.1f}',
    'OVERALL SCORE': '{:.1f}',
    'OVERALL RANK': '{:.1f}'
})

st.markdown('### OUTPUT COUNTRY')
st.dataframe(df1, hide_index=True)


# TABLE 2
df2 = load_excel_data(excel_file, sheet_name2, 'C:L', 2, 14)
df2 = df2.rename(columns={'Unnamed: 2' : 'TICKER'})
df2 = df2.rename(columns={'Unnamed: 3' : 'ETF'})
df2 = df2.rename(columns={'VALUE' : 'COM - VALUE'})
df2 = df2.rename(columns={'QUALITY' : 'COM - QUALITY'})
df2 = df2.rename(columns={'RISK' : 'COM - RISK'})
df2 = df2.rename(columns={'Unnamed: 7' : 'COMPOSITE VALUE'})
df2 = df2.rename(columns={'Unnamed: 8' : 'LIQUIDITY'})
df2 = df2.rename(columns={'Unnamed: 9' : 'MOMENTUM'})
df2 = df2.rename(columns={'Unnamed: 10' : 'CURRENCY'})
df2 = df2.rename(columns={'Unnamed: 11' : 'OVERALL RANK'})

st.markdown('### OUTPUT PPT')
st.dataframe(df2, hide_index=True)
