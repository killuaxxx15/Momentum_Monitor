import pandas as pd
import streamlit as st

st.set_page_config(page_title='India ETF Momentum',
                   page_icon=':bar_chart:')

st.header('Momentum Monitor India ETF')

excel_file = 'INDIA_ETF_MOMENTUM.xlsx'
sheet_name = 'Aset class Rankings'


# Function to apply color based on cell value
def color_cells(val):
    color = '#ffcccc' if val == 'CASH' else ('#ccffcc' if val == 'INVESTED' else '')
    return f'background-color: {color}'

# TABLE 1
df1 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='D:J',
                   header=5,
                   nrows=14)

df1 = df1.rename(columns={'Unnamed: 3' : 'TICKER'})
df1 = df1.rename(columns={'Unnamed: 4' : 'ETF'})
df1 = df1.rename(columns={'Unnamed: 5' : 'Relative Ranking'})
# Applying the styling to the DataFrame
df1 = df1.style.applymap(color_cells)
st.markdown('#### Relative Ranking')
st.dataframe(df1, hide_index=True)



# TABLE 2
df2 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='D:P',
                   header=23,
                   nrows=14)

st.markdown('### Equity Ranking: Momentum + Breadth + Upgrades')
st.dataframe(df2, hide_index=True)








