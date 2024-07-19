import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Set Streamlit page configuration
st.set_page_config(page_title='ETF Dashboard', page_icon=':bar_chart:')

# List of ETF tickers
etf_tickers = [
    "GDX", "COPX", "TAN", "SMH", "EZA", "EPOL", "EWY", "SLV", "EWG", "EWT", "KWEB",
    "PPLT", "FXI", "XLB", "ICLN", "TUR", "MCHI", "EWQ", "ECH", "XME", "CQQQ", "IEV",
    "LIT", "EWL", "GREK", "XLRE", "EPU", "XAR", "EWA", "DEM", "XSOE", "EWJ", "EEM",
    "PCY", "GLD", "EWU", "GNR", "HEDJ", "EWC", "QQQ", "ASHR", "URTH", "EPHE", "RSP",
    "EEMS", "XLF", "SDY", "EELV", "INDY", "EMLC", "SPY", "IWB", "EMB", "QAT", "EMHY",
    "INDA", "DIA", "EWW", "VYM", "EWM", "VTV", "UDN", "DVYE", "VPU", "IWO", "SKYY",
    "VDC", "XLP", "XLY", "HEWJ", "UAE", "LQD", "MOO", "EIDO", "XBI", "XLE", "TLT",
    "KIE", "TIP", "SHY", "DBA", "UNG", "DBC", "KSA", "USO", "ILF", "UUP", "WEAT",
    "VNM", "EWZ", "^VIX", "BNO", "CHIR", "CBON", "EMCB", "LEMB", "VWO", "EWI",
    "^MOVE", "VGK", "XWD.TO", "ITB", "IYT", "IYJ", "QUAL", "IVW", "IAI", "IGE", "IHI",
    "IYH", "IYZ", "^RUT", "EMXC", "PRN", "XLI", "FANG.AX", "AIRR", "SPMO"
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
    ax.plot(relative_performance.index, relative_performance, label=f'{selected_etf} vs {comparison_etf}')
    
    if ma50 is not None:
        ax.plot(ma50.index, ma50, color='orange', linestyle=':', label='50DMA')
    
    if ma200 is not None:
        ax.plot(ma200.index, ma200, color='green', linestyle=':', label='200DMA')

    ax.set_title(f"{selected_etf} vs {comparison_etf}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Relative Performance")
    ax.legend()
    return fig

@st.cache_data
def get_ETF_info(ticker):
    ETF = yf.Ticker(ticker)
    info = ETF.info
    
    try:
        last_price = info['currentPrice']
    except KeyError:
        try:
            last_price = ETF.history(period="1d")['Close'].iloc[-1]
        except IndexError:
            last_price = "N/A"
    
    return {
        "Ticker": ticker,
        "Name": info.get("longName", "N/A"),
        "Price": last_price,
        "P/E Ratio": info.get("trailingPE", "N/A"),
        "52 Week Low": info.get("fiftyTwoWeekLow", "N/A"),
        "52 Week High": info.get("fiftyTwoWeekHigh", "N/A"),
        "Yield": info.get("yield", "N/A"),
        "Net Assets": info.get("totalAssets", "N/A"),
        "NAV": info.get("navPrice", "N/A"),
        "YTD Daily Total Return": info.get("ytdReturn", "N/A"),
        "Beta": info.get("beta3Year", "N/A")
    }

# Streamlit app
st.header("ETF Dashboard")

# Selection options in main content area
col1, col2 = st.columns(2)
with col1:
    default_index = 0
    selected_etf = st.selectbox("Select an ETF", etf_tickers, index=default_index)
with col2:
    time_period = st.selectbox("Select time period", ["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"], index=5)

# Main content
etf_data, etf_full_name = get_etf_data(selected_etf, time_period)
st.subheader(f"{etf_full_name} ({selected_etf})")

# Create and display price chart
price_chart = create_etf_price_chart(etf_data, etf_full_name)
st.pyplot(price_chart)

# Relative performance chart
st.subheader("Relative Performance")
comparison_options = etf_tickers
default_comparison_index = etf_tickers.index("SPY")
comparison_etf = st.selectbox("Compare with", comparison_options, index=default_comparison_index)

# Get data for both ETFs
etf_data1, etf_full_name1 = get_etf_data(selected_etf, time_period)
etf_data2, etf_full_name2 = get_etf_data(comparison_etf, time_period)

# Create and display relative performance chart
rel_perf_chart = create_relative_performance_chart(etf_data1, etf_data2, etf_full_name1, etf_full_name2)
st.pyplot(rel_perf_chart)


# Relative performance chart vs QQQ
default_comparison_index = etf_tickers.index("QQQ")
comparison_etf = st.selectbox("Compare with", comparison_options, index=default_comparison_index)
etf_data2, etf_full_name2 = get_etf_data(comparison_etf, time_period)
rel_perf_chart = create_relative_performance_chart(etf_data1, etf_data2, etf_full_name1, etf_full_name2)
st.pyplot(rel_perf_chart)


# Display ETF information
st.subheader("ETF Information")
ETF_info = [get_ETF_info(ticker) for ticker in etf_tickers]
df = pd.DataFrame(ETF_info)
st.dataframe(df, hide_index=True)
