import pandas as pd
import streamlit as st

st.set_page_config(page_title='ETF Model DEVELOPED',
                   page_icon=':bar_chart:')

st.header('ETF Model DEVELOPED (to be edited)')
st.markdown('#### Updated: 06/03/2024')

excel_file = 'ETF_Model_DEVELOPED.xlsx'
sheet_name1 = 'OUTPUT_COUNTRY'
sheet_name2 = 'OUTPUT_PPT'


def percent_whole_number(val):
    return "{:.0f}%".format(val * 100)



# TABLE 1
df1 = pd.read_excel(excel_file,
                   sheet_name=sheet_name1,
                   usecols='B:N',
                   header=4,
                   nrows=13)

df1 = df1.drop(['Unnamed: 6'], axis=1)
df1 = df1.rename(columns={'Unnamed: 1' : 'TICKER'})
df1 = df1.rename(columns={'Unnamed: 2' : 'ETF'})
df1 = df1.rename(columns={'Unnamed: 7' : 'COMPOSITE VALUE SCORE'})
df1 = df1.rename(columns={'Unnamed: 8' : 'LIQUIDITY'})
df1 = df1.rename(columns={'Unnamed: 11' : 'CURRENCY'})
df1 = df1.rename(columns={'Unnamed: 12' : 'OVERALL SCORE'})
df1 = df1.rename(columns={'Unnamed: 13' : 'OVERALL RANK'})

df1 = df1.style.format({
    'VALUE': '{:.1f}',
    'QUALITY': '{:.1f}',
    'RISK': '{:.1f}',
    'COMPOSITE VALUE SCORE': '{:.1f}',
    'LIQUIDITY': '{:.1f}',
    'SCORE': '{:.1f}',
    'UPGRADES': percent_whole_number,
    'CURRENCY': '{:.1f}',
    'OVERALL SCORE': '{:.1f}',
    'OVERALL RANK': '{:.1f}'
})

st.markdown('### OUTPUT COUNTRY')
st.dataframe(df1, hide_index=True)



# TABLE 2
df2 = pd.read_excel(excel_file,
                   sheet_name=sheet_name2,
                   usecols='C:L',
                   header=2,
                   nrows=13)

st.markdown('### OUTPUT PPT')
st.dataframe(df2, hide_index=True)
