import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set Streamlit page configuration
st.set_page_config(page_title='ETF Dashboard', page_icon=':bar_chart:', layout="wide")

# List of ETF tickers
etf_tickers = [
    '3110.HK', 'ACWX', 'AIRR', 'ARGT', 'ASHR', 'BNO', 'CBON', 'CNYA', 'COPX', 'CQQQ',
    'DBA', 'DBC', 'DEM', 'DIA', 'DVYE', 'ECH', 'EELV', 'EEM', 'EEMS', 'EFA',
    'EFV', 'EIDO', 'EMB', 'EMCB', 'EMHY', 'EMLC', 'EMXC', 'EPHE', 'EPI', 'EPOL',
    'EPU', 'EWA', 'EWC', 'EWD', 'EWG', 'EWI', 'EWJ', 'EWL', 'EWM', 'EWN',
    'EWQ', 'EWT', 'EWU', 'EWW', 'EWY', 'EWZ', 'EZA', 'FANG.AX', 'FXI', 'GDX',
    'GLD', 'GLUX.MI', 'GNR', 'GREK', 'HEDJ', 'HEWJ', 'IAI', 'IAT', 'IBB', 'ICLN',
    'IEV', 'IGE', 'IHI', 'ILF', 'INDA', 'INDY', 'ITA', 'ITB', 'IVE', 'IVW',
    'IWB', 'IWM', 'IWO', 'IYH', 'IYJ', 'IYT', 'IYZ', 'KIE', 'KSA', 'KTEC',
    'KWEB', 'LEMB', 'LIT', 'LQD', 'MCHI', 'MOO', 'PCY', 'PPLT', 'PRN', 'QAT',
    'QQQ', 'QUAL', 'RSP', 'RWR', 'SDY', 'SHY', 'SKYY', 'SLV', 'SMH', 'SMIN',
    'SOXX', 'SPMO', 'SPY', 'TAN', 'THD', 'TIP', 'TLT', 'TUR', 'UAE', 'UDN',
    'UNG', 'URTH', 'USO', 'UUP', 'VDC', 'VGK', 'VNM', 'VNQ', 'VPU', 'VTV',
    'VWO', 'VYM', 'WEAT', 'XAR', 'XBI', 'XLB', 'XLE', 'XLF', 'XLI', 'XLK',
    'XLP', 'XLRE', 'XLU', 'XLV', 'XLY', 'XME', 'XRT', 'XSOE', 'XTL', 'XWD.TO',
    '^MOVE', '^RUT', '^VIX'
]



@st.cache_data
def get_etf_data(etf_ticker, time_period):
    """
    Fetch ETF data, full name, and calculate moving averages if enough data points are available.
    """
    historical_data = yf.download(etf_ticker, period=time_period)
    
    # Get the full name of the ETF
    etf = yf.Ticker(etf_ticker)
    try:
        full_name = etf.info['longName']
    except:
        full_name = etf_ticker  # Use the ticker as fallback if full name is not available
    
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
def create_etf_price_chart(etf_data, etf_full_name):
    """
    Create a price chart for the ETF including moving averages if available.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(etf_data.index, etf_data['Close'], label=f'{selected_etf}')
    
    if etf_data['MA50'].notna().any():
        ax.plot(etf_data.index, etf_data['MA50'], color='orange', linestyle=':', label='50DMA')
    
    if etf_data['MA200'].notna().any():
        ax.plot(etf_data.index, etf_data['MA200'], color='green', linestyle=':', label='200DMA')
    
    ax.set_title(f"{etf_full_name}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    return fig

@st.cache_data
def create_relative_performance_chart(etf_data1, etf_data2, etf_name1, etf_name2):
    """
    Create a relative performance chart comparing two ETFs using aligned dates,
    including 50-day and 200-day moving averages.
    """
    # Ensure date alignment
    common_dates = etf_data1.index.intersection(etf_data2.index)
    aligned_data1 = etf_data1.loc[common_dates]
    aligned_data2 = etf_data2.loc[common_dates]

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
    ax.plot(relative_performance.index, relative_performance, label=f'{etf_name1} vs {etf_name2}')
    
    if ma50 is not None:
        ax.plot(ma50.index, ma50, color='orange', linestyle=':', label='50DMA')
    
    if ma200 is not None:
        ax.plot(ma200.index, ma200, color='green', linestyle=':', label='200DMA')

    ax.set_title(f"{etf_name1} vs {etf_name2}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Relative Performance")
    ax.legend()
    return fig


# Streamlit app
st.header("ETF Dashboard")
time_period = st.selectbox("Select time period", ["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"], index=5)

# Selection options in main content area
col11, col22, col33, col44 = st.columns(4)
with col11:
    default_index = 0
    selected_etf = st.selectbox("Select an ETF", etf_tickers, index=default_index)
with col22:
    comparison_options = etf_tickers
    default_comparison_index = etf_tickers.index("SPY")
    comparison_etf1 = st.selectbox("Compare with", comparison_options, index=default_comparison_index)
with col33:
    comparison_options = etf_tickers
    default_comparison_index = etf_tickers.index("QQQ")
    comparison_etf2 = st.selectbox("Compare with", comparison_options, index=default_comparison_index)
with col44:
    comparison_options = etf_tickers
    default_comparison_index = etf_tickers.index("IWM")
    comparison_etf3 = st.selectbox("Compare with", comparison_options, index=default_comparison_index)

col1, col2, col3, col4 = st.columns([1, 4, 4, 1])
# Main content
with col2:
    etf_data, etf_full_name = get_etf_data(selected_etf, time_period)

    # Create and display price chart
    price_chart = create_etf_price_chart(etf_data, etf_full_name)
    st.pyplot(price_chart)

with col3:
    # Get data for both ETFs
    etf_data1, etf_full_name1 = get_etf_data(selected_etf, time_period)
    etf_data2, etf_full_name2 = get_etf_data(comparison_etf1, time_period)

    # Create and display relative performance chart
    rel_perf_chart_1 = create_relative_performance_chart(etf_data1, etf_data2, selected_etf, comparison_etf1)
    st.pyplot(rel_perf_chart_1)

# Relative performance chart for second comparison
with col2:
    etf_data11, etf_full_name11 = get_etf_data(selected_etf, time_period)
    etf_data22, etf_full_name22 = get_etf_data(comparison_etf2, time_period)
    rel_perf_chart_2 = create_relative_performance_chart(etf_data11, etf_data22, selected_etf, comparison_etf2)
    st.pyplot(rel_perf_chart_2)

# Relative performance chart for third comparison
with col3:
    etf_data111, etf_full_name111 = get_etf_data(selected_etf, time_period)
    etf_data222, etf_full_name222 = get_etf_data(comparison_etf3, time_period)
    rel_perf_chart_3 = create_relative_performance_chart(etf_data111, etf_data222, selected_etf, comparison_etf3)
    st.pyplot(rel_perf_chart_3)
