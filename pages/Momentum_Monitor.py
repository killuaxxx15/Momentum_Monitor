import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config(page_title='Global Momentum',
                   page_icon=':bar_chart:')

st.header('Global Momentum Dashboard')
st.markdown('#### Updated: 15/03/2024')

excel_file = 'Global-macro-rankings-final-15032024.xlsx'
sheet_name = 'Aset class Rankings'


# Function to apply color based on cell value
def color_cells(val):
    color = '#ffcccc' if val == 'CASH' else ('#ccffcc' if val == 'INVESTED' else '')
    return f'background-color: {color}'

def color_cells_1(val):
    color = '#ffcccc' if val >= 5 else ('#ccffcc' if val <= 2 else '#ffffcc')
    return f'background-color: {color}'

def color_cells_2(val):
    color = '#ffcccc' if val > 2 else ('#ccffcc' if val < 0 else '#ffffcc')
    return f'background-color: {color}'

def percent_one_decimal(val):
    return "{:.1f}%".format(val * 100)

def percent_whole_number(val):
    return "{:.0f}%".format(val * 100)


@st.cache
def load_data(excel_file, sheet_name, usecols, header, nrows, names=None):
    return pd.read_excel(excel_file, sheet_name=sheet_name, usecols=usecols, header=header, nrows=nrows, names=names)


# TABLE 1
df1 = load_data(excel_file, sheet_name, 'E:H', 2, 5)
df1 = df1.style.applymap(color_cells, subset=['Above 30 D ', 'Above 60 D', 'Above 200D'])
st.subheader('Table 1: Equity Relative to other Asset Classes')
st.dataframe(df1, hide_index=True)


# TABLE 2
df2 = load_data(excel_file, sheet_name, 'E:J', 13, 12, names=['ETF', 'Relative Ranking', 'Relative Ranking.1', 'Above 30 D ', 'Above 60 D', 'Above 200D'])
df2['Relative Ranking.1'] = np.where(df2['Relative Ranking.1'] >= 8, '🔴', np.where(df2['Relative Ranking.1'] <= 3, '🟢', '🟡'))
df2 = df2.style.applymap(color_cells, subset=['Above 30 D ', 'Above 60 D', 'Above 200D'])
st.subheader('Table 2: Relative Ranking')
st.dataframe(df2, hide_index=True)


# TABLE 3
df3 = load_data(excel_file, sheet_name, 'E:P', 29, 10, names=['Unnamed: 4', 'Relative Ranking', 'U/D', 'Breadth', 'Closeness to 52 week', '3 month return', 'Unnamed: 9', 'U/D.1', 'Breadth.1', 'Closeness to 52 week.1', '3 month return.1', 'Median'])
df3['Relative Ranking'] = np.where(df3['Relative Ranking'] >= 4, '🔴', np.where(df3['Relative Ranking'] <= 0, '🟢', '🟡'))
df3 = df3.drop(['Unnamed: 4', 'Unnamed: 9'], axis=1)
df3 = df3.style.format({
    'U/D': percent_one_decimal,
    'Breadth': percent_whole_number,
    'Closeness to 52 week': percent_one_decimal,
    '3 month return': '{:.1%}',
    'U/D.1': percent_one_decimal,
    'Breadth.1': percent_whole_number,
    'Closeness to 52 week.1': percent_one_decimal,
    '3 month return.1': '{:.1%}',
    'Median': '{:.1f}'
})
st.subheader('Table 3: Equity Ranking: Momentum + Breadth + Upgrades')
st.dataframe(df3, hide_index=True)


# TABLE 4
df4 = load_data(excel_file, sheet_name, 'E:I', 42, 9)
df4 = df4.style.applymap(color_cells, subset=['Above 30D', 'Above 60 D', 'Above 200D'])
st.subheader('Table 4: Equity ETF - MA Signals')
st.dataframe(df4, hide_index=True)


# TABLE 5
df5 = load_data(excel_file, sheet_name, 'K:M', 42, 10, names=['ETF', 'Upgrades 1 month', 'Downgrades 1 month'])
df5 = df5.style.format({'Upgrades 1 month': percent_one_decimal, 'Downgrades 1 month': percent_one_decimal})
st.subheader('Table 5: Equity ETF - Upgrades')
st.dataframe(df5, hide_index=True)


# TABLE 6
df6 = load_data(excel_file, sheet_name, 'E:F', 54, 7, names=['ETF', 'Long Term Forecasts'])
df6 = df6.style.format({'Long Term Forecasts': percent_one_decimal})
st.subheader('Table 6: Long Term Forecasts (above local rates)')
st.dataframe(df6, hide_index=True)
