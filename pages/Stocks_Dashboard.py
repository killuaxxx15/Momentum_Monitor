import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set Streamlit page configuration
st.set_page_config(page_title='Stock Dashboard', page_icon=':bar_chart:', layout="wide")

# List of stock tickers
stock_tickers = [
    "AAPL", "AMZN", "ASML", "AVGO", "COST", "GOOG", "META", "MSFT", "NVDA", "TSLA"
]

# List of major index ETFs for comparison
index_etfs = ["SPY", "QQQ", "IWM"]

@st.cache_data
def get_stock_data(stock_ticker, time_period):
    """
    Fetch stock data, full name, and calculate moving averages if enough data points are available.
    """
    historical_data = yf.download(stock_ticker, period=time_period)
    
    # Get the full name of the stock
    stock = yf.Ticker(stock_ticker)
    try:
        full_name = stock.info['longName']
    except:
        full_name = stock_ticker  # Use the ticker as fallback if full name is not available
    
    # Calculate moving averages only if enough data points are available
    if len(historical_data) >= 50:
        historical_data['MA50'] = historical_data['Close'].rolling(window=50).mean()
    else:
        historical_data['MA50'] = None
    
    if len(historical_data) >= 200:
        historical_data['MA200'] = historical_data['Close'].rolling(window=200).mean()
    else:
        historical_data['MA200'] = None
    
    return historical_data, full_name

@st.cache_data
def create_stock_price_chart(stock_data, stock_full_name):
    """
    Create a price chart for the stock including moving averages if available.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(stock_data.index, stock_data['Close'], label=f'{selected_stock}')
    
    if stock_data['MA50'].notna().any():
        ax.plot(stock_data.index, stock_data['MA50'], color='orange', linestyle=':', label='50DMA')
    
    if stock_data['MA200'].notna().any():
        ax.plot(stock_data.index, stock_data['MA200'], color='green', linestyle=':', label='200DMA')
    
    ax.set_title(f"{stock_full_name}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    return fig

@st.cache_data
def create_relative_performance_chart(stock_data1, stock_data2, stock_name1, stock_name2):
    """
    Create a relative performance chart comparing two stocks using aligned dates,
    including 50-day and 200-day moving averages.
    """
    # Ensure date alignment
    common_dates = stock_data1.index.intersection(stock_data2.index)
    aligned_data1 = stock_data1.loc[common_dates]
    aligned_data2 = stock_data2.loc[common_dates]

    # Calculate relative performance
    relative_performance = aligned_data1['Close'] / aligned_data2['Close']

    # Calculate moving averages for relative performance
    if len(relative_performance) >= 50:
        ma50 = relative_performance.rolling(window=50).mean()
    else:
        ma50 = None

    if len(relative_performance) >= 200:
        ma200 = relative_performance.rolling(window=200).mean()
    else:
        ma200 = None

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(relative_performance.index, relative_performance, label=f'{stock_name1} vs {stock_name2}')
    
    if ma50 is not None:
        ax.plot(ma50.index, ma50, color='orange', linestyle=':', label='50DMA')
    
    if ma200 is not None:
        ax.plot(ma200.index, ma200, color='green', linestyle=':', label='200DMA')

    ax.set_title(f"{stock_name1} vs {stock_name2}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Relative Performance")
    ax.legend()
    return fig

# Streamlit app
st.header("Stock Dashboard")
st.header('Issue with Streamlit. Still fixing.')
time_period = st.selectbox("Select time period", ["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"], index=5)

# Selection options in main content area
col11, col22, col33, col44 = st.columns(4)
with col11:
    default_index = 0
    selected_stock = st.selectbox("Select a Stock", stock_tickers, index=default_index)
with col22:
    comparison_options = index_etfs + stock_tickers
    comparison_stock1 = st.selectbox("Compare with", comparison_options, index=0)
with col33:
    comparison_options = index_etfs + stock_tickers
    comparison_stock2 = st.selectbox("Compare with", comparison_options, index=1)
with col44:
    comparison_options = index_etfs + stock_tickers
    comparison_stock3 = st.selectbox("Compare with", comparison_options, index=2)

col1, col2, col3, col4 = st.columns([1, 4, 4, 1])
# Main content
with col2:
    stock_data, stock_full_name = get_stock_data(selected_stock, time_period)

    # Create and display price chart
    price_chart = create_stock_price_chart(stock_data, stock_full_name)
    st.pyplot(price_chart)

with col3:
    # Get data for both stocks
    stock_data1, stock_full_name1 = get_stock_data(selected_stock, time_period)
    stock_data2, stock_full_name2 = get_stock_data(comparison_stock1, time_period)

    # Create and display relative performance chart
    rel_perf_chart_1 = create_relative_performance_chart(stock_data1, stock_data2, selected_stock, comparison_stock1)
    st.pyplot(rel_perf_chart_1)

# Relative performance chart for second comparison
with col2:
    stock_data1, stock_full_name1 = get_stock_data(selected_stock, time_period)
    stock_data2, stock_full_name2 = get_stock_data(comparison_stock2, time_period)
    rel_perf_chart_2 = create_relative_performance_chart(stock_data1, stock_data2, selected_stock, comparison_stock2)
    st.pyplot(rel_perf_chart_2)

# Relative performance chart for third comparison
with col3:
    stock_data1, stock_full_name1 = get_stock_data(selected_stock, time_period)
    stock_data2, stock_full_name2 = get_stock_data(comparison_stock3, time_period)
    rel_perf_chart_3 = create_relative_performance_chart(stock_data1, stock_data2, selected_stock, comparison_stock3)
    st.pyplot(rel_perf_chart_3)
