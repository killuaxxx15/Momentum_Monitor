import pandas as pd
import streamlit as st

st.set_page_config(page_title='ETF Model EM',
                   page_icon=':bar_chart:')

st.header('ETF Model EM (to be edited)')
st.markdown('#### Updated: 06/03/2024')

excel_file = 'ETF_Model_EM.xlsx'
sheet_name1 = 'OUTPUT_COUNTRY'
sheet_name2 = 'OUTPUT_PPT'


def percent_whole_number(val):
    return "{:.0f}%".format(val * 100)



# TABLE 1
df1 = pd.read_excel(excel_file,
                   sheet_name=sheet_name1,
                   usecols='B:N',
                   header=5,
                   nrows=21)

df1 = df1.drop(['Unnamed: 6'], axis=1)
df1 = df1.rename(columns={'Unnamed: 1' : 'TICKER'})
df1 = df1.rename(columns={'Unnamed: 2' : 'ETF'})
df1 = df1.rename(columns={'Unnamed: 3' : 'VALUE'})
df1 = df1.rename(columns={'Unnamed: 4' : 'QUALITY'})
df1 = df1.rename(columns={'Unnamed: 5' : 'RISK'})
df1 = df1.rename(columns={'Unnamed: 7' : 'COMPOSITE VALUE SCORE'})
df1 = df1.rename(columns={'Unnamed: 8' : 'LIQUIDITY'})
df1 = df1.rename(columns={'Unnamed: 9' : 'SCORE'})
df1 = df1.rename(columns={'Unnamed: 10' : 'UPGRADES'})
df1 = df1.rename(columns={'Unnamed: 11' : 'CURRENCY'})
df1 = df1.rename(columns={'Unnamed: 12' : 'OVERALL SCORE'})
df1 = df1.rename(columns={'Unnamed: 13' : 'OVERALL RANK'})

df1_styled = df1.style.format({
    'UPGRADES': percent_whole_number
})

st.markdown('### OUTPUT COUNTRY')
st.dataframe(df1, hide_index=True)



