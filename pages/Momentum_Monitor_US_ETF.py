import pandas as pd
import streamlit as st

st.set_page_config(page_title='US ETF Momentum Monitor',
                   page_icon=':bar_chart:')

st.header('Momentum Monitor US ETF (lower is better)')
st.markdown('#### Updated: 10/03/2024')

excel_file = 'US_ETF_MOMENTUM_RANKINGS.xlsx'
sheet_name = 'Aset class Rankings'


# Function to apply color based on cell value
def color_cells(val):
    color = '#ffcccc' if val == 'CASH' else ('#ccffcc' if val == 'INVESTED' else '')
    return f'background-color: {color}'

# Define the color_circle function
def color_circle(val):
    if val >= 24:
        return '🔴'  # Red circle if value is greater than or equal to 5
    elif val <= 10:
        return '🟢'  # Green circle if value is less than or equal to 2
    else:
        return '🟡'  # Yellow circle otherwise

def color_circle_1(val):
    if val >= 20:
        return '🔴'  
    elif val <= 7:
        return '🟢'  
    else:
        return '🟡'  

def percent_one_decimal(val):
    return "{:.1f}%".format(val * 100)

def percent_whole_number(val):
    return "{:.0f}%".format(val * 100)



# TABLE 1
df1 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='D:J',
                   header=5,
                   nrows=33)

df1 = df1.rename(columns={'Unnamed: 3' : 'TICKER'})
df1 = df1.rename(columns={'Unnamed: 4' : 'ETF'})
df1 = df1.rename(columns={'Unnamed: 5' : 'Relative Ranking'})
df1 = df1.rename(columns={'Unnamed: 6' : 'Relative Ranking.1'})
df1['Relative Ranking.1'] = df1['Relative Ranking.1'].apply(color_circle)
df1 = df1.style.applymap(color_cells, subset=['Above 30 D ', 'Above 60 D', 'Above 200D'])
st.markdown('### Relative Ranking')
st.dataframe(df1, hide_index=True)



# TABLE 2
df2 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='D:P',
                   header=42,
                   nrows=33)

df2 = df2.rename(columns={'Unnamed: 3' : 'TICKER'})
df2 = df2.rename(columns={'Unnamed: 4' : 'ETF'})
df2 = df2.rename(columns={'Clsoeness to 52 week' : 'Closeness to 52 week.1'})
df2 = df2.rename(columns={'median' : 'Median'})
relative_ranking = df2['Relative ranking']
df2 = df2.drop(['Relative ranking'], axis=1)
df2 = df2.drop(['Unnamed: 9'], axis=1)
df2.insert(2, "Relative Ranking", relative_ranking)
df2['Relative Ranking'] = df2['Relative Ranking'].apply(color_circle_1)
df2 = df2.style.format({
      'U/D': percent_one_decimal, 
      'Breadth': percent_whole_number, 
      'Closeness to 52 week': percent_one_decimal,
      '3 month return': '{:.1f}',
      'Median': '{:.1f}'
})
st.markdown('### Equity Ranking: Momentum + Breadth + Upgrades')
st.dataframe(df2, hide_index=True)



# TABLE 3
df3 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='D:G',
                   header=80,
                   nrows=33)

#df3 = df3.rename(columns={'TICKER.1' : 'TICKER'})
#df3 = df3.rename(columns={'ETF.1' : 'ETF'})
df3 = df3.style.format({'Upgrades 1 month': percent_one_decimal, 'Downgrades 1 month': percent_one_decimal})
st.markdown('### Equity ETF - Upgrades')
st.dataframe(df3, hide_index=True)










