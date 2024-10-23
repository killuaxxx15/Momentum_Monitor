import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from zoneinfo import ZoneInfo  # For timezone handling

# Set Streamlit page configuration
st.set_page_config(page_title='ETF Asset Class Performance', page_icon=':bar_chart:')

# Define ticker sets
us_related_etf_tickers = ['SPY', 'DIA', 'QQQ', 'IJH', 'IJR', 'IWB', 'IWM', 'IWV', 'IVW', 'IJK', 'IJT', 'IVE', 'IJJ', 'IJS', 'DVY', 'RSP']
us_sectors_etf_tickers = ['XLY', 'XLP', 'XLE', 'XLF', 'XLV', 'XLI', 'XLB', 'XLRE', 'XLK', 'XLC', 'XLU', 'DBC', 'DBA', 'USO', 'UNG', 'GLD', 'SLV', 'SHY', 'IEF' ,'TLT', 'AGG', 'BND', 'TIP']
global_etf_tickers = ['EWA', 'EWZ', 'EWC', 'ASHR', 'EWQ', 'EWG', 'EWH', 'PIN', 'EWI', 'EWJ', 'EWW', 'EWP', 'EIS', 'EWU', 'EFA', 'EEM', 'IOO', 'BKF', 'CWI', 'FXB', 'FXE', 'FXY']

@st.cache_data(ttl=3600)  # Cache data for 1 hour
def get_ETF_info(ticker):
    try:
        ETF = yf.Ticker(ticker)
        info = ETF.info

        # Define dates as strings to avoid timezone issues
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
        ytd_start = datetime(datetime.now().year, 1, 1).strftime('%Y-%m-%d')

        # Get historical data
        hist_data = yf.download(ticker, start=start_date, end=end_date, progress=False)

        if hist_data.empty:
            return {
                "ETF": ticker,
                "Name": info.get("longName", "N/A"),
                "YTD Return": np.nan,
                "1-Month Return": np.nan,
                "1-Week Return": np.nan
            }

        # YTD calculation - use string indexing
        ytd_data = hist_data[hist_data.index >= ytd_start]
        if not ytd_data.empty:
            ytd_return = (ytd_data['Adj Close'].iloc[-1] / ytd_data['Adj Close'].iloc[0] - 1)
        else:
            ytd_return = np.nan

        # Calculate rolling returns
        current_price = hist_data['Adj Close'].iloc[-1]
        month_ago_price = hist_data['Adj Close'].shift(21).iloc[-1]
        week_ago_price = hist_data['Adj Close'].shift(5).iloc[-1]

        rolling_1month = (current_price / month_ago_price - 1) if not pd.isna(month_ago_price) else np.nan
        rolling_1week = (current_price / week_ago_price - 1) if not pd.isna(week_ago_price) else np.nan

        return {
            "ETF": ticker,
            "Name": info.get("longName", "N/A"),
            "YTD Return": ytd_return,
            "1-Month Return": rolling_1month,
            "1-Week Return": rolling_1week
        }
    except Exception as e:
        st.warning(f"Error fetching data for {ticker}: {str(e)}")
        return {
            "ETF": ticker,
            "Name": "Error",
            "YTD Return": np.nan,
            "1-Month Return": np.nan,
            "1-Week Return": np.nan
        }

def process_etf_info(etf_info_list):
    processed_info = []
    for info in etf_info_list:
        processed_item = info.copy()
        # Process percentage columns
        for key in ['YTD Return', '1-Month Return', '1-Week Return']:
            try:
                if isinstance(info[key], (int, float)) and not pd.isna(info[key]):
                    processed_item[key] = round(float(info[key]) * 100, 2)
                else:
                    processed_item[key] = np.nan
            except (TypeError, ValueError):
                processed_item[key] = np.nan
        processed_info.append(processed_item)
    return processed_info

def color_scale(val):
    try:
        if pd.isna(val):
            return ''
        
        # Define the range for color mapping
        vmin, vmax = -10, 10
        norm = plt.Normalize(vmin, vmax)
        
        # Create a custom colormap
        colors = ['#FF9999', '#FFFF99', '#90EE90']
        n_bins = 10
        cmap = LinearSegmentedColormap.from_list("custom", colors, N=n_bins)
        
        # Get the RGB color based on the value
        rgb = cmap(norm(val))
        
        # Convert RGB to hex
        hex_color = '#{:02x}{:02x}{:02x}'.format(int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))
        
        return f'background-color: {hex_color}'
    except:
        return ''

def create_etf_table(tickers):
    with st.spinner('Fetching ETF data...'):
        ETF_info = [get_ETF_info(ticker) for ticker in tickers]
        processed_ETF_info = process_etf_info(ETF_info)
        df = pd.DataFrame(processed_ETF_info)
        
        # Convert columns to numeric, coercing errors to NaN
        numeric_columns = ['YTD Return', '1-Month Return', '1-Week Return']
        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        # Create a formatting dictionary
        format_dict = {
            'YTD Return': '{:.2f}%',
            '1-Month Return': '{:.2f}%',
            '1-Week Return': '{:.2f}%',
        }

        return df.style.format(format_dict, na_rep='N/A').map(color_scale, subset=numeric_columns)

# Main Streamlit app
st.header('ETF Asset Class Performance YTD, 1-Month, and 1-Week')

try:
    st.subheader('US Related')
    us_related_etf_table = create_etf_table(us_related_etf_tickers)
    st.dataframe(us_related_etf_table, hide_index=True)

    st.subheader('US Sectors, Commodities & Fixed Income')
    us_sectors_etf_table = create_etf_table(us_sectors_etf_tickers)
    st.dataframe(us_sectors_etf_table, hide_index=True)

    st.subheader('Global')
    global_etf_table = create_etf_table(global_etf_tickers)
    st.dataframe(global_etf_table, hide_index=True)
except Exception as e:
    st.error(f"An error occurred: {str(e)}")
