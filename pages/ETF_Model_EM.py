import pandas as pd
import streamlit as st

st.set_page_config(page_title='ETF Model EM',
                   page_icon=':bar_chart:')

st.header('ETF Model EM')
st.markdown('#### Updated: 06/03/2024')

excel_file = 'ETF_Model_EM.xlsx'
sheet_name1 = 'OUTPUT_COUNTRY'
sheet_name2 = 'OUTPUT_PPT'

# TABLE 1
df1 = pd.read_excel(excel_file,
                   sheet_name=sheet_name1,
                   usecols='B:N',
                   header=5,
                   nrows=21)

df1 = df1.rename(columns={'Unnamed: 1' : 'TICKER'})
df1 = df1.rename(columns={'Unnamed: 2' : 'ETF'})
df1 = df1.rename(columns={'Unnamed: 3' : 'VALUE'})
df1 = df1.rename(columns={'Unnamed: 4' : 'QUALITY'})
df1 = df1.rename(columns={'Unnamed: 5' : 'RISK'})
df1 = df1.rename(columns={'Unnamed: 6' : 'COMPOSITE VALUE SCORE'})
df1 = df1.rename(columns={'Unnamed: 7' : 'LIQUIDITY'})
df1 = df1.rename(columns={'Unnamed: 8' : 'SCORE'})
df1 = df1.rename(columns={'Unnamed: 9' : 'UPGRADES'})
df1 = df1.rename(columns={'Unnamed: 10' : 'CURRENCY'})
df1 = df1.rename(columns={'Unnamed: 11' : 'OVERALL SCORE'})
df1 = df1.rename(columns={'Unnamed: 12' : 'OVERALL RANK'})


st.markdown('### OUTPUT COUNTRY')
st.dataframe(df1, hide_index=True)



