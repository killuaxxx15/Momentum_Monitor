import pandas as pd
import streamlit as st

st.set_page_config(page_title='Global Momentum',
                   page_icon=':bar_chart:')

st.header('Global Momentum Dashboard')
st.markdown('#### Updated: 15/03/2024')

excel_file = 'Global-macro-rankings-final-15032024.xlsx'
sheet_name = 'Aset class Rankings'

# Decorator to cache data loading function
@st.cache
def load_excel_data(file_name, sheet, use_columns, header_row, num_rows):
    return pd.read_excel(file_name, sheet_name=sheet, usecols=use_columns, header=header_row, nrows=num_rows)

# Function to apply color based on cell value
def color_cells(val):
    color = '#ffcccc' if val == 'CASH' else ('#ccffcc' if val == 'INVESTED' else '')
    return f'background-color: {color}'

def color_cells_1(val):
    color = '#ffcccc' if val >= 5 else ('#ccffcc' if val <=2 else '#ffffcc')
    return f'background-color: {color}'

# Define the color_circle function
def color_circle(val):
    if val >= 8:
        return '🔴'  
    elif val <= 3:
        return '🟢'  
    else:
        return '🟡'  

def color_cells_2(val):
    color = '#ffcccc' if val > 2 else ('#ccffcc' if val < 0 else '#ffffcc')
    return f'background-color: {color}'
  
def color_circle_1(val):
    if val >= 4:
        return '🔴'  
    elif val <= 0:
        return '🟢'  
    else:
        return '🟡' 

def percent_one_decimal(val):
    return "{:.1f}%".format(val * 100)

def percent_whole_number(val):
    return "{:.0f}%".format(val * 100)




# TABLE 1
df1 = load_excel_data(excel_file, sheet_name, 'E:H', 2, 5)
df1 = df1.style.applymap(color_cells, subset=['Above 30 D ', 'Above 60 D', 'Above 200D'])
st.markdown('### Table 1: Equity Relative to other Asset Classes')
st.dataframe(df1, hide_index=True)



# TABLE 2
df2 = load_excel_data(excel_file, sheet_name, 'E:J', 13, 12)
df2 = df2.rename(columns={'Unnamed: 4' : 'ETF'})
df2 = df2.rename(columns={'Unnamed: 5' : 'Relative Ranking'})
df2 = df2.rename(columns={'Unnamed: 6' : 'Relative Ranking.1'})
df2['Relative Ranking.1'] = df2['Relative Ranking.1'].apply(color_circle)
df2 = df2.style.applymap(color_cells, subset=['Above 30 D ', 'Above 60 D', 'Above 200D'])
st.markdown('### Table 2: Relative Ranking')
st.dataframe(df2, hide_index=True)




# TABLE 3
df3 = load_data(excel_file, sheet_name, 'E:P', 29, 10)
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
df3['Relative Ranking'] = df3['Relative Ranking'].apply(color_circle_1)
df3 = df3.style.format({
      'U/D': percent_one_decimal, 
      'Breadth': percent_whole_number, 
      'Closeness to 52 week': percent_one_decimal,
      '3 month return': '{:.1f}',
      'Median': '{:.1f}'
})
st.markdown('### Table 3: Equity Ranking: Momentum + Breadth + Upgrades')
st.dataframe(df3, hide_index=True)




# TABLE 4
df4 = load_data(excel_file, sheet_name, 'E:I', 42, 9)
df4 = df4.style.applymap(color_cells, subset=['Above 30D', 'Above 60 D', 'Above 200D'])
st.markdown('### Table 4: Equity ETF - MA Signals')
st.dataframe(df4, hide_index=True)




# TABLE 5
df5 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='K:M',
                   header=42,
                   nrows=10)
df5 = load_data(excel_file, sheet_name, 'K:M', 42, 10)
df5 = df5.rename(columns={'Unnamed: 10' : 'ETF'})
df5 = df5.style.format({'Upgrades 1 month': percent_one_decimal, 'Downgrades 1 month': percent_one_decimal})
st.markdown('### Table 5: Equity ETF - Upgrades')
st.dataframe(df5, hide_index=True)




# TABLE 6
df6 = load_data(excel_file, sheet_name, 'E:F', 54, 7)
df6 = df6.rename(columns={'Table 6 : Long Term forecasts ( above local rates )' : 'ETF'})
df6 = df6.rename(columns={'Unnamed: 5' : 'Long Term Forecasts'})
df6 = df6.style.format({'Long Term Forecasts': percent_one_decimal})
st.markdown('### Table 6: Long Term Forecasts (above local rates)')
st.dataframe(df6, hide_index=True)
