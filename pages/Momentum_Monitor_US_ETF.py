import pandas as pd
import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title='US ETF Momentum Monitor', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('Momentum Monitor US ETF (lower is better)')

# Display the last update date
st.markdown('#### Updated: 10/08/2024')

# Define Excel file and sheet name variables
excel_file = 'US_ETF_MOMENTUM_RANKINGS_10_08_2024.xlsx'
sheet_name = 'Aset class Rankings'

# Cache data loading function for better performance
@st.cache
def load_excel_data(file_name, sheet, use_columns, header_row, num_rows):
    return pd.read_excel(file_name, sheet_name=sheet, usecols=use_columns, header=header_row, nrows=num_rows)

# Function to apply background color based on cell value
def color_cells(val):
    color = '#ffcccc' if val == 'CASH' else ('#ccffcc' if val == 'INVESTED' else '')
    return f'background-color: {color}'

# Define function to display colored circle based on cell value
def color_circle(val, lowest_10, highest_10):
    if val in lowest_10:
        return '🟢'
    elif val in highest_10:
        return '🔴'
    else:
        return '🟡'

# Format percentage with one decimal place
def percent_one_decimal(val):
    return "{:.1f}%".format(val * 100)

# Format percentage as whole number
def percent_whole_number(val):
    return "{:.0f}%".format(val * 100)


# TABLE 1
df1 = load_excel_data(excel_file, sheet_name, 'D:K', 5, 34)
df1 = df1.rename(columns={'Unnamed: 3' : 'TICKER'})
df1 = df1.rename(columns={'Unnamed: 4' : 'ETF'})
df1 = df1.rename(columns={'Unnamed: 7' : 'Current Ranking.1'})
ranking_1 = df1['Current Ranking.1']
# Sort the 'Current Ranking.1' series in ascending order
sorted_ranking_1 = ranking_1.sort_values()

# Determine the thresholds for the lowest 10 and highest 10 values
lowest_10 = sorted_ranking_1.head(10).values
highest_10 = sorted_ranking_1.tail(10).values

# Apply the color_circle_1 function to each value in the 'Relative Ranking' column
df1['Current Ranking.1'] = ranking_1.apply(color_circle, args=(lowest_10, highest_10))

df1 = df1.style.applymap(color_cells, subset=['Above 30 D ', 'Above 60 D', 'Above 200D'])
st.markdown('### Relative Ranking')
st.dataframe(df1, hide_index=True)


# TABLE 2
df2 = load_excel_data(excel_file, sheet_name, 'D:P', 42, 34)
df2 = df2.rename(columns={'Unnamed: 3' : 'TICKER'})
df2 = df2.rename(columns={'Unnamed: 4' : 'ETF'})
df2 = df2.rename(columns={'Clsoeness to 52 week' : 'Closeness to 52 week.1'})
df2 = df2.rename(columns={'median' : 'Median'})
relative_ranking = df2['Relative ranking']
df2 = df2.drop(['Relative ranking'], axis=1)
df2 = df2.drop(['Unnamed: 9'], axis=1)
df2.insert(2, "Relative Ranking", relative_ranking)

# Sort the 'Relative Ranking' series in ascending order
sorted_relative_ranking = relative_ranking.sort_values()
# Determine the thresholds for the lowest 10 and highest 10 values
lowest_10 = sorted_relative_ranking.head(10).values
highest_10 = sorted_relative_ranking.tail(10).values
# Apply the color_circle_1 function to each value in the 'Relative Ranking' column
df2['Relative Ranking'] = relative_ranking.apply(color_circle, args=(lowest_10, highest_10))
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
df3 = load_excel_data(excel_file, sheet_name, 'D:G', 80, 34)
df3 = df3.style.format({'Upgrades 1 month': percent_one_decimal, 'Downgrades 1 month': percent_one_decimal})
st.markdown('### Equity ETF - Upgrades')
st.dataframe(df3, hide_index=True)
