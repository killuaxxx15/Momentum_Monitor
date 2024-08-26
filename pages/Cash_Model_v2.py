import pandas as pd
import streamlit as st
import numpy as np

# Set Streamlit page configuration
st.set_page_config(page_title='Cash Model', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('Cash Model')

# Display the last update date
st.markdown('#### from Excel file from Alvaro')

# Define Excel file and sheet name variables
excel_file = 'CashSignal_Streamlit.xlsm'
sheet_name = 'CashSignals'

# Cache data loading function for better performance
@st.cache_data
def load_excel_data(file_name, sheet, header_row, num_rows):
    # Define the columns to use
    cols_to_use = list(range(1, 11)) + [18, 27]  # B to K (1-10), S (18), AB (27)
    return pd.read_excel(file_name, sheet_name=sheet, usecols=cols_to_use, header=header_row, nrows=num_rows)

# Format percentage as whole number with one decimal place, handling non-numeric values
def percent_whole_number(val):
    if pd.isna(val) or not isinstance(val, (int, float)):
        return val
    return f"{val * 100:.1f}%"

# Format as whole number without decimal points
def whole_number(val):
    if pd.isna(val) or not isinstance(val, (int, float)):
        return val
    return f"{int(val)}"

# New function to format as percentage whole number without decimals
def percent_whole_number_no_decimal(val):
    if pd.isna(val) or not isinstance(val, (int, float)):
        return val
    return f"{int(val * 100)}%"

# Conditional formatting function
def color_signal_1(val):
    if val == 1:
        return 'background-color: #90EE90'  # Green
    return ''

def color_signal_2(val):
    if val == 'INVESTED' or (isinstance(val, (int, float)) and val > 0.5):
        return 'background-color: #90EE90'  # Green
    elif val == 'CAUTIOUS' or (isinstance(val, (int, float)) and 0.25 <= val <= 0.5):
        return 'background-color: #FFFF99'  # Yellow
    elif val == 'CASH' or (isinstance(val, (int, float)) and val < 0.25):
        return 'background-color: #FF9999'  # Red
    return ''

# New function to highlight specific rows
def highlight_rows(row):
    if row.name in [0, 9, 13, 16, 19]:  # Adjust for 0-based index
        return ['background-color: #ADD8E6'] * len(row)  # Light blue
    return [''] * len(row)


# TABLE 1
df1 = load_excel_data(excel_file, sheet_name, 2, 33)
df1 = df1.fillna('')

# Format specific cells as percentages
df1.iloc[0:20, df1.columns.get_loc('Level')] = df1.iloc[0:20, df1.columns.get_loc('Level')].apply(lambda x: f'{x:.0%}' if isinstance(x, (int, float)) else x)
df1.iloc[20, df1.columns.get_loc('Level')] = f'{df1.iloc[20, df1.columns.get_loc("Level")]:.2f}' if isinstance(df1.iloc[20, df1.columns.get_loc('Level')], (int, float)) else df1.iloc[20, df1.columns.get_loc('Level')]
df1.iloc[21, df1.columns.get_loc('Level')] = f'{df1.iloc[21, df1.columns.get_loc("Level")]:.1f}' if isinstance(df1.iloc[21, df1.columns.get_loc('Level')], (int, float)) else df1.iloc[21, df1.columns.get_loc('Level')]
df1.iloc[22, df1.columns.get_loc('Level')] = f'{df1.iloc[22, df1.columns.get_loc("Level")]:.0f}' if isinstance(df1.iloc[22, df1.columns.get_loc('Level')], (int, float)) else df1.iloc[22, df1.columns.get_loc('Level')]

# Apply formatting
format_dict = {}
for col in df1.columns:
    if col in ['50DMA', '100DMA', '200DMA']:
        format_dict[col] = percent_whole_number
    elif col in ['50DMA.1', '100DMA.1', '200DMA.1']:
        format_dict[col] = whole_number
    elif col in ['Current Reading', 'Short Term Trend', '1 Week Ago', '1M Ago']:
        format_dict[col] = percent_whole_number_no_decimal

styled_df = df1.style.format(format_dict)

# Apply conditional formatting
signal_columns_1 = ['50DMA.1', '100DMA.1', '200DMA.1']  # Adjust this list as needed
for col in signal_columns_1:
    if col in df1.columns:
        styled_df = styled_df.applymap(color_signal_1, subset=[col])

signal_columns_2 = ['Current Reading', 'Short Term Trend', '1 Week Ago', '1M Ago']  # Adjust this list as needed
for col in signal_columns_2:
    if col in df1.columns:
        styled_df = styled_df.applymap(color_signal_2, subset=[col])

# Apply row highlighting
styled_df = styled_df.apply(highlight_rows, axis=1)

st.markdown('### US Sentiment Signals')
st.dataframe(styled_df, hide_index=True)
