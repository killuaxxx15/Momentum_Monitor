import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set Streamlit page configuration
st.set_page_config(page_title='Stock Dashboard', page_icon=':bar_chart:', layout="wide")

# List of stock tickers
stock_tickers = [
    "AAPL", "AMZN", "MSFT", "NVDA", "AVGO", "META", "GOOG", "COST", "TSLA", "ASML"
]

# List of major index ETFs for comparison
index_etfs = ["SPY", "QQQ"]

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
    ax.plot(relative_performance.index, relative_performance, label=f'{selected_stock} vs {comparison_stock}')
    
    if ma50 is not None:
        ax.plot(ma50.index, ma50, color='orange', linestyle=':', label='50DMA')
    
    if ma200 is not None:
        ax.plot(ma200.index, ma200, color='green', linestyle=':', label='200DMA')

    ax.set_title(f"{selected_stock} vs {comparison_stock}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Relative Performance")
    ax.legend()
    return fig

# Function to get company info
@st.cache_data
def get_company_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    
    try:
        last_price = info['currentPrice']
    except KeyError:
        try:
            last_price = stock.history(period="1d")['Close'].iloc[-1]
        except IndexError:
            last_price = np.nan
    
    return {
        "Ticker": ticker,
        "Name": info.get("longName", "N/A"),
        "Price": last_price,
        "P/E Ratio": info.get("trailingPE", np.nan),
        "52 Week Low": info.get("fiftyTwoWeekLow", np.nan),
        "52 Week High": info.get("fiftyTwoWeekHigh", np.nan),
        "Market Cap": info.get("marketCap", np.nan),
        "Div Yield": info.get("dividendYield", np.nan),
        "Beta": info.get("beta", np.nan),
        "EPS": info.get("trailingEps", np.nan)
    }

@st.cache_data
def process_company_info(company_info_list):
    for info in company_info_list:
        # Process numeric columns
        for key in ['Price', 'P/E Ratio', '52 Week Low', '52 Week High', 'Beta', 'EPS']:
            if info[key] != "N/A" and not pd.isna(info[key]):
                info[key] = round(float(info[key]), 2)
            else:
                info[key] = np.nan

        # Process percentage columns
        for key in ['Div Yield']:
            if info[key] != "N/A" and not pd.isna(info[key]):
                info[key] = round(float(info[key]) * 100, 2)  # Convert to percentage
            else:
                info[key] = np.nan

        # Process Market Cap
        if info['Market Cap'] != "N/A" and not pd.isna(info['Market Cap']):
            info['Market Cap'] = float(info['Market Cap']) / 1_000_000_000 # Convert to billions
        else:
            info['Market Cap'] = np.nan

    return company_info_list

# Streamlit app
st.header("Stock Dashboard")

# Selection options in main content area
col11, col22, col33 = st.columns(3)
with col11:
    default_index = 0
    selected_stock = st.selectbox("Select a Stock", stock_tickers, index=default_index)
with col22:
    time_period = st.selectbox("Select time period", ["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"], index=5)
with col33:
    comparison_options = index_etfs + stock_tickers
    comparison_stock = st.selectbox("Compare with", comparison_options, index=0)
    


col1, col2 = st.columns(2)
# Main content
with col1:
    stock_data, stock_full_name = get_stock_data(selected_stock, time_period)
    st.subheader(f"{stock_full_name} ({selected_stock})")

    # Create and display price chart
    price_chart = create_stock_price_chart(stock_data, stock_full_name)
    st.pyplot(price_chart)

with col2:
    # Relative performance chart
    st.subheader("Relative Performance")
    
    # Get data for both stocks
    stock_data1, stock_full_name1 = get_stock_data(selected_stock, time_period)
    stock_data2, stock_full_name2 = get_stock_data(comparison_stock, time_period)

    # Create and display relative performance chart
    rel_perf_chart = create_relative_performance_chart(stock_data1, stock_data2, stock_full_name1, stock_full_name2)
    st.pyplot(rel_perf_chart)


col111, col222, col333 = st.columns([1, 2, 1])
# Relative performance chart vs QQQ

# Use col2 and col3 to display the image
with col222:
    # Display the image across both col2 and col3
    comparison_stock = st.selectbox("Compare with", comparison_options, index=1)
    stock_data2, stock_full_name2 = get_stock_data(comparison_stock, time_period)
    rel_perf_chart = create_relative_performance_chart(stock_data1, stock_data2, stock_full_name1, stock_full_name2)
    st.pyplot(rel_perf_chart)

    # Display company information
    st.subheader("Company Information")
    company_info = [get_company_info(ticker) for ticker in stock_tickers]
    process_Company_info = process_company_info(company_info)
    df = pd.DataFrame(process_Company_info)

    # Convert columns to numeric, coercing errors to NaN
    numeric_columns = ['Price', 'P/E Ratio', '52 Week Low', '52 Week High', 'Div Yield', 'Beta', 'EPS']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Create a formatting dictionary
    format_dict = {
        'Price': '{:.2f}',
        'P/E Ratio': '{:.2f}',
        '52 Week Low': '{:.2f}',
        '52 Week High': '{:.2f}',
        'Div Yield': '{:.2f}%',
        'Beta': '{:.2f}',
        'EPS': '{:.2f}',
        'Market Cap': lambda x: f'{x:.2f}B' if pd.notnull(x) else 'N/A'
    }

    st.dataframe(df.style.format(format_dict), hide_index=True)
