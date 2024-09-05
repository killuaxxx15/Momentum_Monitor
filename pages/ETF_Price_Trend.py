import streamlit as st
import pandas as pd
from datetime import datetime
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import yfinance as yf


def Logarithmic_regression(df):
    # Create a copy of the DataFrame to ensure we're not working on a slice
    df = df[df['Close'].notna()].copy()
    
    df['price_y'] = np.log(df['Close'])
    df['x'] = np.arange(len(df))
    
    try:
        b, a = np.polyfit(df['x'], df['price_y'], 1)
    except Exception as e:
        b, a = 0, 0
    
    df['priceTL'] = b * df['x'] + a
    df['y-TL'] = df['price_y'] - df['priceTL']
    sd = np.std(df['y-TL'])
    df['SD'] = sd
    df['TL-2SD'] = df['priceTL'] - 2 * sd
    df['TL-SD'] = df['priceTL'] - sd
    df['TL+2SD'] = df['priceTL'] + 2 * sd
    df['TL+SD'] = df['priceTL'] + sd
    
    return df

def plot_chart(ax, df):
    RAINBOWCOLOR1 = 'hotpink'
    RAINBOWCOLOR2 = 'orange'
    RAINBOWCOLOR3 = 'gold'
    RAINBOWCOLOR4 = 'yellowgreen'
    RAINBOWCOLOR5 = 'lightgreen'
      
    ax.plot(df['Date'], df['price_y'], color='black', linewidth=0.5)
    ax.plot(df['Date'], df['TL+2SD'], color=RAINBOWCOLOR1, linewidth=0.5)
    ax.plot(df['Date'], df['TL+SD'], color=RAINBOWCOLOR2, linewidth=0.5)
    ax.plot(df['Date'], df['priceTL'], color=RAINBOWCOLOR3, linewidth=0.5)
    ax.plot(df['Date'], df['TL-SD'], color=RAINBOWCOLOR4, linewidth=0.5)
    ax.plot(df['Date'], df['TL-2SD'], color=RAINBOWCOLOR5, linewidth=0.5)

    ax.fill_between(df['Date'], df['TL+2SD'], df['TL+SD'], facecolor=RAINBOWCOLOR2, alpha=0.6, edgecolor=None, linewidth=0)
    ax.fill_between(df['Date'], df['TL+SD'], df['priceTL'], facecolor=RAINBOWCOLOR3, alpha=0.6, edgecolor=None, linewidth=0)
    ax.fill_between(df['Date'], df['priceTL'], df['TL-SD'], facecolor=RAINBOWCOLOR4, alpha=0.6, edgecolor=None, linewidth=0)
    ax.fill_between(df['Date'], df['TL-SD'], df['TL-2SD'], facecolor=RAINBOWCOLOR5, alpha=0.6, edgecolor=None, linewidth=0)

    return ax

@st.cache_data
def stock_screener(tickers, startdate):
    figcol = 3
    figrow = math.ceil(len(tickers) / figcol)
    
    fig_height = figrow * 3
    fig_width = figcol * 4
    
    dynamic_dpi = 300
    dynamic_fontsize = 8

    fig, axes = plt.subplots(figrow, figcol, figsize=(fig_width, fig_height), dpi=dynamic_dpi, squeeze=False, sharey=False, sharex='col')

    all_stock_data = yf.download(tickers, start=startdate, interval='1d')
    all_stock_data = all_stock_data.reset_index()     
    
    for i, s in enumerate(tickers):
        tickerDf = pd.DataFrame()
        ax = axes[i // figcol, i % figcol]
        
        tickerDf['Date'] = all_stock_data['Date']
        tickerDf['Close'] = all_stock_data['Close'][s]
        
        titlecolor = 'black'
        facecolor = 'white'

        tickerDf = Logarithmic_regression(tickerDf)
        ax = plot_chart(ax, tickerDf)
        
        pct_change = 0

        if len(tickerDf) > 3:
            if np.isnan(tickerDf['Close'].iloc[-1]):
                current_price = tickerDf['Close'].iloc[-2]
                previous_price = tickerDf['Close'].iloc[-3]    
            else:
                current_price = tickerDf['Close'].iloc[-1]
                previous_price = tickerDf['Close'].iloc[-2]    
                    
            pct_change = ((current_price - previous_price) / previous_price) * 100

        if (pct_change >= 0):
            todaytrendsymbol = '⇧'
            titlecolor = 'darkgreen'
            facecolor = 'palegreen'
        else:
            todaytrendsymbol = '⇩'
            titlecolor = 'red'
            facecolor = 'mistyrose'

        ax.patch.set_facecolor(facecolor)
        ax.grid(True, color='silver', linewidth=0.5)
        ax.tick_params(axis='x', labelrotation=90)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m'))
        ax.xaxis.set_tick_params(labelsize=dynamic_fontsize)
        ax.yaxis.set_tick_params(labelsize=dynamic_fontsize)
        
        title = f"{s}\n{current_price:.2f}{todaytrendsymbol}{pct_change:.2f}%"
        ax.set_title(title, fontweight='bold', color=titlecolor, fontsize=dynamic_fontsize)

    for j in range(len(tickers), figrow * figcol):
        ax = axes[j // figcol, j % figcol]
        ax.axis('off')
    
    plt.subplots_adjust(wspace=0.3, hspace=0.4)
 
    today = datetime.now().strftime("%Y-%m-%d")
    fig.suptitle(f"ETF Screener\n{startdate}~{today}", fontweight="bold", y=1.02, fontsize=dynamic_fontsize + 2)
    fig.tight_layout()
    
    return fig


# Set Streamlit page configuration
st.set_page_config(page_title='ETF Price Trend with Logarithmic Regression', page_icon=':bar_chart:', layout="wide")

# Display header for the dashboard
st.header("ETF Price Trend with Logarithmic Regression")

# Fixed list of ETF tickers
etf_tickers = [
    "EIDO", "EPOL", "EWM", "EWT", "EWW", "EWY", "EWZ", "EZA", "GREK", "TUR", "UAE", "KSA", "ARGT",
    "THD", "EPHE", "ECH", "INDA", "COPX", "PICK", "MOO", "PRN", "EWL", "EWG", "EWU", "EWC", "EWA",
    "EWQ", "EWN", "EWD", "EWI", "EWJ", "QQQ", "SPY", "XLF", "XLV", "XLY", "XLP", "XLB", "XLE", "XLU",
    "ITA", "ITB", "CNYA", "MCHI", "KTEC", "KWEB", "IWM", "SOXX", "EFV", "EEM", "EFA", "3110.HK", 
    "EPI", "GDX", "SMIN"
]

# Allow user to select start date
start_date = st.date_input("Select Start Date", value=pd.to_datetime("2024-01-01"))

# Automatically generate and display the chart
try:
    with st.spinner("Generating ETF Screener..."):
        fig = stock_screener(etf_tickers, start_date)
        st.pyplot(fig)
    st.success("ETF screener chart has been generated successfully.")
except Exception as e:
    st.error(f"An error occurred: {e}")
