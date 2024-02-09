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

def color_cells_1(val):
    color = '#ffcccc' if val >= 5 else ('#ccffcc' if val <=2 else '#ffffcc')
    return f'background-color: {color}'

def color_cells_2(val):
    color = '#ffcccc' if val > 7 else ('#ccffcc' if val <=4 else '#ffffcc')
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
df1 = df1.drop(['Unnamed: 6'], axis=1)
df1 = df1.style.applymap(color_cells, subset=['Above 30 D ', 'Above 60 D', 'Above 200D'])\
               .applymap(color_cells_1, subset=['Relative Ranking'])
st.markdown('### Relative Ranking')
st.dataframe(df1, hide_index=True)



# TABLE 2
df2 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='D:P',
                   header=23,
                   nrows=14)

df2 = df2.rename(columns={'Unnamed: 3' : 'TICKER'})
df2 = df2.rename(columns={'Unnamed: 4' : 'ETF'})
df2 = df2.rename(columns={'Clsoeness to 52 week' : 'Closeness to 52 week.1'})
relative_ranking = df2['Relative ranking']
df2 = df2.drop(['Relative ranking'], axis=1)
df2 = df2.drop(['Unnamed: 9'], axis=1)
df2.insert(2, "Relative Ranking", relative_ranking)
df2 = df2.style.applymap(color_cells_2, subset=['Relative Ranking'])
st.markdown('### Equity Ranking: Momentum + Breadth + Upgrades')
st.dataframe(df2, hide_index=True)



# TABLE 3
df3 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='D:I',
                   header=42,
                   nrows=14)

df3 = df3.drop(['Unnamed: 5'], axis=1)
df3 = df3.style.applymap(color_cells)
st.markdown('### Equity ETF - MA Signals')
st.dataframe(df3, hide_index=True)




# TABLE 4
df4 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='K:N',
                   header=42,
                   nrows=14)

df4 = df4.rename(columns={'TICKER.1' : 'TICKER'})
df4 = df4.rename(columns={'ETF.1' : 'ETF'})
st.markdown('### Equity ETF - Upgrades')
st.dataframe(df4, hide_index=True)










