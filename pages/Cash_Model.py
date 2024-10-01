import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Set Streamlit page configuration
st.set_page_config(page_title='Cash Model', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('Cash Model')

# Display the last update date
st.markdown('#### Updated: 27/09/2024')

# Define Excel file and sheet name variables
excel_file = 'CashSignal_Streamlit_27_09_2024.xlsx'
sheet_name_us = 'CashSignals'
sheet_name_world = 'WorldxUSSignals'
sheet_name_qqq = 'QQQ'
sheet_name_factors = 'Factors'

# Cache data loading function for better performance
@st.cache_data
def load_excel_data(file_name, sheet, header_row, num_rows):
    # Define the columns to use
    cols_to_use = list(range(1, 11)) + [18, 27]  # B to K (1-10), S (18), AB (27)
    return pd.read_excel(file_name, sheet_name=sheet, usecols=cols_to_use, header=header_row, nrows=num_rows)

@st.cache_data
def load_excel_data_2(file_name, sheet, header_row, num_rows):
    # Define the columns to use
    cols_to_use = [5] + list(range(10, 20))  # F (5), K to T (10-20)
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
    if val == 'INVESTED' or (isinstance(val, (int, float)) and val > 0.75):
        return 'background-color: #90EE90'  # Green
    elif val == 'CAUTIOUS' or (isinstance(val, (int, float)) and 0.25 <= val <= 0.75):
        return 'background-color: #FFFF99'  # Yellow
    elif val == 'CASH' or (isinstance(val, (int, float)) and val < 0.25):
        return 'background-color: #FF9999'  # Red
    elif val == 'IMPROVING':
        return 'background-color: #ADD8E6'  # Blue
    return ''

# New function to highlight specific rows
def highlight_rows(row):
    if row.name in [0, 9, 13, 16, 19]:  # Adjust for 0-based index
        return ['background-color: #ADD8E6'] * len(row)  # Light blue
    return [''] * len(row)

# New function to highlight specific rows
def highlight_rows_2(row):
    if row.name in [0, 7, 14]:  # Adjust for 0-based index
        return ['background-color: #ADD8E6'] * len(row)  # Light blue
    return [''] * len(row)

def color_scale(val):
    if pd.isna(val) or not isinstance(val, (int, float)):
        return ''
    
    color_map = {
        1: '#90EE90',  # Light green
        2: '#B8E6B8',  # Lighter green
        3: '#FFFFFF',  # White
        4: '#FFE6E6',  # Very very light red
        5: '#FFCCCC',  # Very light red
        6: '#FF9999'   # Light red
    }
    
    val = int(val)  # Ensure the value is an integer
    if val in color_map:
        return f'background-color: {color_map[val]}'
    return ''


def process_and_style_dataframe(df):
    df = df.fillna('')
    df = df.rename(columns={'Unnamed: 1' : ' '})

    # Format specific cells as percentages
    df.iloc[0:20, df.columns.get_loc('Level')] = df.iloc[0:20, df.columns.get_loc('Level')].apply(lambda x: f'{x:.0%}' if isinstance(x, (int, float)) else x)
    df.iloc[20, df.columns.get_loc('Level')] = f'{df.iloc[20, df.columns.get_loc("Level")]:.2f}' if isinstance(df.iloc[20, df.columns.get_loc('Level')], (int, float)) else df.iloc[20, df.columns.get_loc('Level')]
    df.iloc[21, df.columns.get_loc('Level')] = f'{df.iloc[21, df.columns.get_loc("Level")]:.1f}' if isinstance(df.iloc[21, df.columns.get_loc('Level')], (int, float)) else df.iloc[21, df.columns.get_loc('Level')]
    df.iloc[22, df.columns.get_loc('Level')] = f'{df.iloc[22, df.columns.get_loc("Level")]:.0f}' if isinstance(df.iloc[22, df.columns.get_loc('Level')], (int, float)) else df.iloc[22, df.columns.get_loc('Level')]

    # Apply formatting
    format_dict = {}
    for col in df.columns:
        if col in ['50DMA', '100DMA', '200DMA']:
            format_dict[col] = percent_whole_number
        elif col in ['50DMA.1', '100DMA.1', '200DMA.1']:
            format_dict[col] = whole_number
        elif col in ['Current Reading', 'Short Term Trend', '1 Week Ago', '1M Ago']:
            format_dict[col] = percent_whole_number_no_decimal

    styled_df = df.style.format(format_dict)

    # Apply conditional formatting
    signal_columns_1 = ['50DMA.1', '100DMA.1', '200DMA.1']  # Adjust this list as needed
    for col in signal_columns_1:
        if col in df.columns:
            styled_df = styled_df.applymap(color_signal_1, subset=[col])

    signal_columns_2 = ['Current Reading', 'Short Term Trend', '1 Week Ago', '1M Ago']  # Adjust this list as needed
    for col in signal_columns_2:
        if col in df.columns:
            styled_df = styled_df.applymap(color_signal_2, subset=[col])

    # Apply row highlighting and bold text
    styled_df = styled_df.apply(highlight_rows, axis=1)

    return styled_df

def color_scale_trend_summary(val):
    if pd.isna(val):
        return ''
    
    if val == 1 or val == 'Positive' or val == 'Outperformer':
        return 'background-color: #90EE90'  # Light green
    elif val in ['Cautious', 'Outperformer AND Losing', 'Underperformer AND Gaining']:
        return 'background-color: #FFFF99'  # Light yellow
    elif val == 'Underperformer':
        return 'background-color: #FF9999'  # Light red
    return ''

def process_and_style_dataframe_2(df):
    # Rename the columns
    column_rename_map = {
        'Unnamed: 5': ' ',
        'Unnamed: 11': 'Relative Rankings.2',
        'Unnamed: 12': 'Relative Rankings.3',
        'Unnamed: 13': 'Relative Rankings.4',
        'Unnamed: 15': 'Trend.2',
        'Unnamed: 16': 'Trend.3',
        'Unnamed: 18': 'Summary.2',
        'Unnamed: 19': 'Summary.3',
    }
    df = df.rename(columns=column_rename_map)

    # Apply row highlighting
    styled_df_2 = df.style.apply(highlight_rows_2, axis=1)

    # Apply color scale to specific columns
    ranking_columns = ['Relative Rankings', 'Relative Rankings.2', 'Relative Rankings.3', 'Relative Rankings.4']
    for col in ranking_columns:
        if col in df.columns:
            styled_df_2 = styled_df_2.applymap(color_scale, subset=[col])

    # Apply color scale to Trend and Summary columns
    trend_summary_columns = ['Trend', 'Trend.2', 'Trend.3', 'Summary', 'Summary.2', 'Summary.3']
    for col in trend_summary_columns:
        if col in df.columns:
            styled_df_2 = styled_df_2.applymap(color_scale_trend_summary, subset=[col])

    return styled_df_2

# Load and process US data
df_us = load_excel_data(excel_file, sheet_name_us, 2, 33)
styled_df_us = process_and_style_dataframe(df_us)

# Load and process World ex-US data
df_world = load_excel_data(excel_file, sheet_name_world, 2, 33)
styled_df_world = process_and_style_dataframe(df_world)

# Load and process QQQ data
df_qqq = load_excel_data(excel_file, sheet_name_qqq, 2, 33)
styled_df_qqq = process_and_style_dataframe(df_qqq)

# Load and process Factors
df_factors = load_excel_data_2(excel_file, sheet_name_factors, 13, 21)
styled_df_factors = process_and_style_dataframe_2(df_factors)

# Display US Sentiment Signals
st.markdown('### US Sentiment Signals')
st.dataframe(styled_df_us, hide_index=True)

# Display World ex-US Sentiment Signals
st.markdown('### World ex-US Sentiment Signals')
st.dataframe(styled_df_world, hide_index=True)

# Display NASDAQ Sentiment Signals
st.markdown('### NASDAQ Sentiment Signals')
st.dataframe(styled_df_qqq, hide_index=True)

# Display Factors
st.markdown('### Factors')
st.dataframe(styled_df_factors, hide_index=True)
