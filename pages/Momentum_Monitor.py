import pandas as pd
import streamlit as st

st.set_page_config(page_title='Global Momentum',
                   page_icon=':bar_chart:')

st.header('Global Momentum Dashboard')

excel_file = 'sample.xlsx'
sheet_name = 'Aset class Rankings'


# Function to apply color based on cell value
def color_cells(val):
    color = '#ffcccc' if val == 'CASH' else ('#ccffcc' if val == 'INVESTED' else '')
    return f'background-color: {color}'

def color_cells_1(val):
    color = '#ffcccc' if val >= 5 else ('#ccffcc' if val <=2 else '#ffffcc')
    return f'background-color: {color}'

def color_cells_2(val):
    color = '#ffcccc' if val >= 4 else ('#ccffcc' if val < 0 else '#ffffcc')
    return f'background-color: {color}'

def percent_one_decimal(val):
    return "{:.1f}%".format(val * 100)

def percent_whole_number(val):
    return "{:.0f}%".format(val * 100)




# TABLE 1
df1 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:H',
                   header=2,
                   nrows=5)

df1 = df1.style.applymap(color_cells, subset=['Above 30 D ', 'Above 60 D', 'Above 200D'])
st.markdown('### Table 1: Equity Relative to other Asset Classes')
st.dataframe(df1, hide_index=True)



# TABLE 2
df2 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:J',
                   header=13,
                   nrows=11)

df2 = df2.rename(columns={'Unnamed: 4' : 'ETF'})
df2 = df2.rename(columns={'Unnamed: 5' : 'Relative Ranking'})
df2 = df2.drop(['Unnamed: 6'], axis=1)
df2 = df2.style.applymap(color_cells, subset=['Above 30 D ', 'Above 60 D', 'Above 200D'])\
               .applymap(color_cells_1, subset=['Relative Ranking'])
st.markdown('### Table 2: Relative Ranking')
st.dataframe(df2, hide_index=True)




# TABLE 3
df3 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:P',
                   header=28,
                   nrows=9)

df3 = df3.rename(columns={'Unnamed: 5' : 'U/D'})
df3 = df3.rename(columns={'Unnamed: 6' : 'Breadth'})
df3 = df3.rename(columns={'Unnamed: 7' : 'Closeness to 52 week'})
df3 = df3.rename(columns={'Unnamed: 8' : '3 month return'})
df3 = df3.rename(columns={'Unnamed: 10' : 'U/D.1'})
df3 = df3.rename(columns={'Unnamed: 11' : 'Breadth.1'})
df3 = df3.rename(columns={'Unnamed: 12' : 'Closeness to 52 week.1'})
df3 = df3.rename(columns={'Unnamed: 13' : '3 month return.1'})
df3 = df3.rename(columns={'Unnamed: 14' : 'Median'})
df3 = df3.rename(columns={'Unnamed: 15' : 'Relative Ranking'})
relative_ranking = df3['Relative Ranking']
df3 = df3.drop(['Relative Ranking'], axis=1)
df3 = df3.drop(['Unnamed: 9'], axis=1)
df3.insert(1, "Relative Ranking", relative_ranking)
df3 = df3.style.applymap(color_cells_2, subset=['Relative Ranking'])\
    .format({
      'U/D': percent_one_decimal, 
      'Breadth': percent_whole_number, 
      'Closeness to 52 week': percent_one_decimal,
      '3 month return': '{:.1f}',
      'median': '{:.1f}',
      'Relative Ranking': '{:.1f}'
})
st.markdown('### Table 3: Equity Ranking: Momentum + Breadth + Upgrades')
st.dataframe(df3, hide_index=True)




# TABLE 4
df4 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:I',
                   header=40,
                   nrows=9)

st.markdown('### Table 4: Equity ETF - MA Signals')
st.dataframe(df4, hide_index=True)




# TABLE 5
df5 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='K:M',
                   header=40,
                   nrows=10)

st.markdown('### Table 5: Equity ETF - Upgrades')
st.dataframe(df5, hide_index=True)




# TABLE 6
df6 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:F',
                   header=52,
                   nrows=6)

st.markdown('### Table 6: Long Term Forecasts (above local rates)')
st.dataframe(df6, hide_index=True)









