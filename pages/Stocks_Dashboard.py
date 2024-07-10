import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Set Streamlit page configuration
st.set_page_config(page_title='Stocks Dashboard', page_icon=':bar_chart:')

# List of stock tickers
tickers = ["AAPL", "AMZN", "MSFT", "NVDA", "AVGO", "META", "GOOG", "COST", "TSLA", "ASML"]

# Function to get stock data
def get_stock_data(ticker, period):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    
    # Calculate 50-day and 200-day moving averages
    hist['MA50'] = hist['Close'].rolling(window=50).mean()
    hist['MA200'] = hist['Close'].rolling(window=200).mean()
    
    return hist

# Function to get company info
def get_company_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    
    # Use the same fallback method for the last price
    try:
        last_price = info['currentPrice']
    except KeyError:
        last_price = stock.history(period="1d")['Close'].iloc[-1]
    
    return {
        "Ticker": ticker,
        "Symbol Name": info.get("longName", "N/A"),
        "Last Price": last_price,
        "Market Cap": info.get("marketCap", "N/A"),
        "P/E Ratio": info.get("trailingPE", "N/A"),
        "52 Week High": info.get("fiftyTwoWeekHigh", "N/A"),
        "52 Week Low": info.get("fiftyTwoWeekLow", "N/A")
    }

# Function to create stock price chart
def create_price_chart(data, ticker):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data.index, data['Close'], label=ticker)
    ax.plot(data.index, data['MA50'], color='orange', linestyle=':', label='50 DMA')
    ax.plot(data.index, data['MA200'], color='green', linestyle=':', label='200 DMA')
    ax.set_title(f"{ticker}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    return fig

# Function to create relative performance chart
def create_relative_performance_chart(data1, data2, ticker1, ticker2):
    relative_perf = (data1['Close'] / data1['Close'].iloc[0]) / (data2['Close'] / data2['Close'].iloc[0])
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(relative_perf.index, relative_perf, label=f'{ticker1} vs {ticker2}')
    ax.set_title(f"Relative Performance: {ticker1} vs {ticker2}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Relative Performance")
    ax.legend()
    return fig

# Streamlit app
st.header("Stocks Dashboard")

# Selection options in main content area
col1, col2 = st.columns(2)
with col1:
    selected_ticker = st.selectbox("Select a stock", tickers, index=tickers.index("AAPL"))
with col2:
    period = st.selectbox("Select time period", ["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"], index=5)

# Main content
st.subheader(f"{selected_ticker} Stock Price")
data = get_stock_data(selected_ticker, period)

# Create and display price chart
price_chart = create_price_chart(data, selected_ticker)
st.pyplot(price_chart)

# Display company information
st.subheader("Company Information")
company_info = [get_company_info(ticker) for ticker in tickers]
df = pd.DataFrame(company_info)
st.dataframe(df, hide_index=True)

# Relative performance chart
st.subheader("Relative Performance")
compare_options = ["SPY"] + tickers
compare_ticker = st.selectbox("Compare with", compare_options, index=0)

# Get data for both tickers
data1 = get_stock_data(selected_ticker, period)
data2 = get_stock_data(compare_ticker, period)

# Create and display relative performance chart
rel_perf_chart = create_relative_performance_chart(data1, data2, selected_ticker, compare_ticker)
st.pyplot(rel_perf_chart)
