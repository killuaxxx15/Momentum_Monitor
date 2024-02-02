import pandas as pd
import streamlit as st

st.set_page_config(page_title='Global Momentum',
                   page_icon=':bar_chart:')

st.header('To be edited')

excel_file = 'sample.xlsx'
sheet_name = 'Aset class Rankings'



# Function to apply color based on cell value
def color_cells(val):
    color = '#ffcccc' if val == 'CASH' else ('#ccffcc' if val == 'INVESTED' else '')
    return f'background-color: {color}'


df1 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:H',
                   header=2,
                   nrows=5)

# Applying the styling to the DataFrame
df1 = df1.style.applymap(color_cells)
st.markdown('#### Table 1: Equity Relative to other Asset Classes')
st.dataframe(df1, hide_index=True)



df2 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:J',
                   header=11,
                   nrows=13)


df2 = df2.style.applymap(color_cells)
st.markdown('#### Table 2: Relative Ranking')
st.write(df2)







df3 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:P',
                   header=27,
                   nrows=10)

st.markdown('#### Table 3: Equity Ranking: Momentum + Breadth + Upgrades')
st.dataframe(df3, hide_index=True)



df4 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:I',
                   header=40,
                   nrows=9)

df4 = df4.style.applymap(color_cells)
st.markdown('#### Table 4: Equity ETF - MA Signals')
st.dataframe(df4, hide_index=True)


df5 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='K:M',
                   header=40,
                   nrows=10)

st.markdown('#### Table 5: Equity ETF - Upgrades')
st.dataframe(df5, hide_index=True)


df6 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:F',
                   header=52,
                   nrows=6)

st.markdown('#### Table 6: Long Term Forecasts (above local rates)')
st.dataframe(df6, hide_index=True)
