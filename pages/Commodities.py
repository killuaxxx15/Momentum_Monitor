import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Set Streamlit page configuration
st.set_page_config(page_title='Commodities', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('Commodities')

# Display the last update date
st.markdown('#### Updated: 01/10/2024')

# Define Excel file and sheet name variables
excel_file = 'CashSignal_Streamlit_27_09_2024.xlsx'
sheet_name_commodities = 'Commodities'

def highlight_rows(row):
    if row.name in [0, 22]:  # Adjust for 0-based index
        return ['background-color: #ADD8E6'] * len(row)  # Light blue
    return [''] * len(row)

def color_scale(val):
    if pd.isna(val) or not isinstance(val, (int, float)):
        return ''
    
    # Define the range for color mapping
    vmin, vmax = 1, 21
    
    # Create a custom colormap
    light_green = '#90EE90'
    very_light_green = '#E6FFE6'
    very_light_red = '#FFE6E6'
    light_red = '#FF9999'
    
    cmap = LinearSegmentedColormap.from_list("custom", [
        light_green,
        very_light_green,
        very_light_red,
        light_red
    ], N=9)
    
    # Normalize the value
    norm_val = (val - vmin) / (vmax - vmin)
    
    # Get the RGB color based on the normalized value
    rgb = cmap(norm_val)
    
    # Convert RGB to hex
    hex_color = '#{:02x}{:02x}{:02x}'.format(int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))
    
    return f'background-color: {hex_color}'

def color_scale_trend_summary(val):
    if pd.isna(val):
        return ''
    
    if val == 1 or val == 'Positive' or val == 'Outperformer':
        return 'background-color: #90EE90'  # Light green
    elif val in ['Cautious', 'Outperformer AND Losing', 'Underperformer AND Gaining']:
        return 'background-color: #FFFF99'  # Light yellow
    elif val == 'Underperformer' or val == 'Negative':
        return 'background-color: #FF9999'  # Light red
    return ''

def color_scale_2(val):
    if pd.isna(val) or not isinstance(val, (int, float)):
        return ''
    
    # Define colors for each value
    color_map = {
        1: '#90EE90',  # Light green
        2: '#B8E6B8',  # Lighter green
        3: '#FFB3BA',  # Light pink
        4: '#FF9999'   # Light red
    }
    
    val = int(val)  # Ensure the value is an integer
    if val in color_map:
        return f'background-color: {color_map[val]}'
    return ''

def process_and_style_dataframe(df):
    # Rename the columns
    column_rename_map = {
        'Unnamed: 5': ' ',
        'Unnamed: 6': '  ',
        'Unnamed: 12': 'Relative Rankings.2',
        'Unnamed: 13': 'Relative Rankings.3',
        'Unnamed: 14': 'Relative Rankings.4',
        'Unnamed: 16': 'Trend.2',
        'Unnamed: 17': 'Trend.3',
        'Unnamed: 19': 'Summary.2',
        'Unnamed: 20': 'Summary.3',
    }
    df = df.rename(columns=column_rename_map)

    df = df.fillna('')

    # Apply row highlighting
    df = df.style.apply(highlight_rows, axis=1)

    # Apply color scale to specific columns
    ranking_columns = ['Relative Rankings', 'Relative Rankings.2', 'Relative Rankings.3', 'Relative Rankings.4']
    for col in ranking_columns:
        if col in df.columns:
            # Apply color_scale to rows 1-21
            df = df.applymap(color_scale, subset=pd.IndexSlice[1:22, col])
            # Apply color_scale_1_to_4 to rows 23-26
            df = df.applymap(color_scale_2, subset=pd.IndexSlice[23:27, col])

    # Apply color scale to Trend and Summary columns
    trend_summary_columns = ['Trend', 'Trend.2', 'Trend.3', 'Summary', 'Summary.2', 'Summary.3']
    for col in trend_summary_columns:
        if col in df.columns:
            df = df.applymap(color_scale_trend_summary, subset=[col])

    return df


# Cache data loading function for better performance
@st.cache_data
def load_excel_data(file_name, sheet, header_row, num_rows):
    # Define the columns to use
    cols_to_use = [5, 6] + list(range(11, 21))  # F and G (5, 6), L to U (10-21)
    return pd.read_excel(file_name, sheet_name=sheet, usecols=cols_to_use, header=header_row, nrows=num_rows)

# Load and process Factors
df_commodities = load_excel_data(excel_file, sheet_name_commodities, 13, 27)
styled_df_commodities = process_and_style_dataframe(df_commodities)

st.dataframe(styled_df_commodities, hide_index=True)
