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
st.markdown('#### Updated: 19/10/2024')

# Define Excel file and sheet name variables
excel_file = 'CashSignal_Streamlit_19_10_2024.xlsx'
sheet_name_commodities = 'Commodities'
sheet_name_us = 'CashSignals'


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

def color_signal_3(val):
    if val in ['Outperformer', 'Positive - Above 50DMA']:
        return 'background-color: #90EE90'  # Green
    elif val in ['Outperformer & Losing', 'Underperformer & Gaining', 'Cautious - Above 200DMA but Below 50DMA']:
        return 'background-color: #FFFF99'  # Yellow
    elif val in ['Underperformer', 'Negative - Below 50DMA and Below 200']:
        return 'background-color: #FF9999'  # Red
    return ''

def process_and_style_dataframe(df):
    # Rename the columns
    column_rename_map = {
        '1M.1': '1M',
        '3M.1': '3M',
        '6M.1': '6M',
        '12M.1': '12M',
        'Relative': 'Summary'
    }
    df = df.rename(columns=column_rename_map)

    # Create a style object
    styled_df = df.style

    # Apply color scale to specific columns
    ranking_columns = ['1M', '3M', '6M', '12M']
    for col in ranking_columns:
        if col in df.columns:
            # Apply color_scale to entire columns
            styled_df = styled_df.apply(lambda x: pd.Series([color_scale(v) for v in x], index=x.index), 
                                      subset=[col])
            
    # Apply color scale to specific columns
    ranking_columns = ['50MA', '100MA', '200MA', 'Short Term Trend', 'Trend', 'Summary']
    for col in ranking_columns:
        if col in df.columns:
            # Apply color_scale_trend_summary to entire columns
            styled_df = styled_df.apply(lambda x: pd.Series([color_scale_trend_summary(v) for v in x], index=x.index), 
                                      subset=[col])

    return styled_df

def process_and_style_dataframe_2(df):
    # Rename the columns
    column_rename_map = {
        '1M.1': '1M',
        '3M.1': '3M',
        '6M.1': '6M',
        '12M.1': '12M',
        'Relative': 'Summary'
    }
    df = df.rename(columns=column_rename_map)

    # Create a style object
    styled_df = df.style

    # Apply color scale to specific columns
    ranking_columns = ['1M', '3M', '6M', '12M']
    for col in ranking_columns:
        if col in df.columns:
            # Apply color_scale_2 to entire columns
            styled_df = styled_df.apply(lambda x: pd.Series([color_scale_2(v) for v in x], index=x.index), 
                                      subset=[col])
            
    # Apply color scale to specific columns
    ranking_columns = ['50MA', '100MA', '200MA', 'Short Term Trend', 'Trend', 'Summary']
    for col in ranking_columns:
        if col in df.columns:
            # Apply color_scale_trend_summary to entire columns
            styled_df = styled_df.apply(lambda x: pd.Series([color_scale_trend_summary(v) for v in x], index=x.index), 
                                      subset=[col])

    return styled_df


def process_and_style_dataframe_3(df):
    df = df.fillna('')

    # Create a style object
    styled_df = df.style

    styled_df = styled_df.map(color_signal_3)
            

    return styled_df


# Cache data loading function for better performance
@st.cache_data
def load_excel_data(file_name, sheet, header_row, num_rows):
    # Define the columns to use
    cols_to_use = [5, 6] + list(range(11, 21))  # F and G (5, 6), L to U (10-21)
    return pd.read_excel(file_name, sheet_name=sheet, usecols=cols_to_use, header=header_row, nrows=num_rows)

# Load and process Factors
df_commodities = load_excel_data(excel_file, sheet_name_commodities, 14, 21)
styled_df_commodities = process_and_style_dataframe(df_commodities)
st.dataframe(styled_df_commodities, hide_index=True)


@st.cache_data
def load_excel_data(file_name, sheet, header_row, num_rows):
    # Define the columns to use
    cols_to_use = [6] + list(range(11, 21))  # F and G (5, 6), L to U (10-21)
    return pd.read_excel(file_name, sheet_name=sheet, usecols=cols_to_use, header=header_row, nrows=num_rows)

# Load and process Factors
df_commodities = load_excel_data(excel_file, sheet_name_commodities, 36, 4)
styled_df_commodities = process_and_style_dataframe_2(df_commodities)
st.dataframe(styled_df_commodities, hide_index=True)


@st.cache_data
def load_excel_data_3(file_name, sheet, header_row, num_rows):
    # Define the columns to use
    cols_to_use = list(range(1, 3))  # B to C (1-2)
    return pd.read_excel(file_name, sheet_name=sheet, usecols=cols_to_use, header=header_row, nrows=num_rows)

# Load and process Rationale
df_rationale = load_excel_data_3(excel_file, sheet_name_us, 69, 9)
styled_df_rationale = process_and_style_dataframe_3(df_rationale)
st.dataframe(styled_df_rationale, hide_index=True)
