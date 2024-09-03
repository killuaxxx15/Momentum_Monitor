import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Set Streamlit page configuration
st.set_page_config(page_title='ETF Asset Class Performance', page_icon=':bar_chart:')

# Define ticker sets
us_related_etf_tickers = ['SPY', 'DIA', 'QQQ', 'IJH', 'IJR', 'IWB', 'IWM', 'IWV', 'IVW', 'IJK', 'IJT', 'IVE', 'IJJ', 'IJS', 'DVY', 'RSP']
us_sectors_etf_tickers = ['XLY', 'XLP', 'XLE', 'XLF', 'XLV', 'XLI', 'XLB', 'XLRE', 'XLK', 'XLC', 'XLU', 'DBC', 'DBA', 'USO', 'UNG', 'GLD', 'SLV', 'SHY', 'IEF' ,'TLT', 'AGG', 'BND', 'TIP']
global_etf_tickers = ['EWA', 'EWZ', 'EWC', 'ASHR', 'EWQ', 'EWG', 'EWH', 'PIN', 'EWI', 'EWJ', 'EWW', 'EWP', 'EIS', 'EWU', 'EFA', 'EEM', 'IOO', 'BKF', 'CWI', 'FXB', 'FXE', 'FXY']

@st.cache_data
def get_ETF_info(ticker):
    ETF = yf.Ticker(ticker)
    info = ETF.info

    # Define end date and start date for data fetch
    end_date = datetime.now().strftime("%Y-%m-%d")
    ytd_start_date = "2023-12-29"  # YTD start date

    # Get historical data
    hist_data = yf.download(ticker, start=ytd_start_date, end=end_date)

    if not hist_data.empty:
        # YTD calculation
        ytd_start_price = hist_data.loc[ytd_start_date:, 'Adj Close'].iloc[0]

        # MTD calculation
        current_month = datetime.now().replace(day=1)
        prev_month_end = current_month - timedelta(days=1)
        mtd_start_price = hist_data.loc[:prev_month_end.strftime("%Y-%m-%d"), 'Adj Close'].iloc[-1]

        # This Week calculation
        current_weekday = datetime.now().weekday()
        prev_week_end = datetime.now() - timedelta(days=current_weekday+3)  # Go back to previous Friday
        week_start_price = hist_data.loc[:prev_week_end.strftime("%Y-%m-%d"), 'Adj Close'].iloc[-1]

        current_price = hist_data['Adj Close'].iloc[-1]

        ytd_return = (current_price - ytd_start_price) / ytd_start_price
        mtd_return = (current_price - mtd_start_price) / mtd_start_price
        week_return = (current_price - week_start_price) / week_start_price
    else:
        ytd_return = mtd_return = week_return = np.nan

    return {
        "ETF": ticker,
        "Name": info.get("longName", "N/A"),
        "YTD Return": ytd_return,
        "MTD Return": mtd_return,
        "This Week Return": week_return
    }

def process_etf_info(etf_info_list):
    for info in etf_info_list:        
        # Process percentage columns
        for key in ['YTD Return', 'MTD Return', 'This Week Return']:
            if info[key] != "N/A" and not pd.isna(info[key]):
                info[key] = round(float(info[key]) * 100, 2)  # Convert to percentage
            else:
                info[key] = np.nan

    return etf_info_list

def color_scale(val):
    if pd.isna(val) or val == 0:
        return ''
    
    # Define the range for color mapping
    vmin, vmax = -10, 10
    norm = plt.Normalize(vmin, vmax)
    
    # Create a custom colormap with a lighter shade of red
    colors = ['#FF9999', '#FFFF99', '#90EE90']  # Light red, light yellow, light green
    n_bins = 10  # Number of color gradations
    cmap = LinearSegmentedColormap.from_list("custom", colors, N=n_bins)
    
    # Get the RGB color based on the value
    rgb = cmap(norm(val))
    
    # Convert RGB to hex
    hex_color = '#{:02x}{:02x}{:02x}'.format(int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))
    
    return f'background-color: {hex_color}'

def create_etf_table(tickers):
    ETF_info = [get_ETF_info(ticker) for ticker in tickers]
    processed_ETF_info = process_etf_info(ETF_info)
    df = pd.DataFrame(processed_ETF_info)

    # Convert columns to numeric, coercing errors to NaN
    numeric_columns = ['YTD Return', 'MTD Return', 'This Week Return']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Create a formatting dictionary
    format_dict = {
        'YTD Return': '{:.2f}%',
        'MTD Return': '{:.2f}%',
        'This Week Return': '{:.2f}%',
    }

    return df.style.format(format_dict).map(color_scale, subset=numeric_columns)

# Main Streamlit app
st.header('ETF Asset Class Performance YTD, MTD, and This Week')

st.subheader('US Related')
us_related_etf_table = create_etf_table(us_related_etf_tickers)
st.dataframe(us_related_etf_table, hide_index=True)

st.subheader('US Sectors, Commodities & Fixed Income')
us_sectors_etf_table = create_etf_table(us_sectors_etf_tickers)
st.dataframe(us_sectors_etf_table, hide_index=True)

st.subheader('Global')
global_etf_table = create_etf_table(global_etf_tickers)
st.dataframe(global_etf_table, hide_index=True)
