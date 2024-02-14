import pandas as pd
import streamlit as st

st.set_page_config(page_title='US ETF Momentum Monitor',
                   page_icon=':bar_chart:')

st.header('Momentum Monitor US ETF')

excel_file = 'US_ETF_MOMENTUM.xlsx'
sheet_name = 'Aset class Rankings'


# Function to apply color based on cell value
def color_cells(val):
    color = '#ffcccc' if val == 'CASH' else ('#ccffcc' if val == 'INVESTED' else '')
    return f'background-color: {color}'

# Define the color_circle function
def color_circle(val):
    if val >= 5:
        return '🔴'  # Red circle if value is greater than or equal to 5
    elif val <= 2:
        return '🟢'  # Green circle if value is less than or equal to 2
    else:
        return '🟡'  # Yellow circle otherwise

def color_circle_1(val):
    if val >= 4:
        return '🔴'  
    elif val < 0:
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


















