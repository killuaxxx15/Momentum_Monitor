import pandas as pd
import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title='Sentiment Data', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('Sentiment Data')

# Display the last update date
st.markdown('#### Updated: 05/07/2024')

# Define Excel file and sheet name variables
excel_file = 'Sentiment_Data_05_07_2024.xlsx'
sheet_name = 'Sheet1'

# Cache data loading function for better performance
@st.cache
def load_excel_data(file_name, sheet, use_columns, header_row, num_rows):
    return pd.read_excel(file_name, sheet_name=sheet, usecols=use_columns, header=header_row, nrows=num_rows)

# TABLE 1
df1 = load_excel_data(excel_file, sheet_name, 'F:K', 10, 5)
df1 = df1.fillna('')
# Format specific cells as percentages
df1.iloc[1:3, 2] = df1.iloc[1:3, 2].apply(lambda x: f'{x:.2%}')
df1.iloc[4:5, 2] = df1.iloc[4:5, 2].apply(lambda x: f'{x:.2%}')
#df1.iloc[1:3, 3] = df1.iloc[1:3, 3].apply(lambda x: f'{x:.0%}')
#df1.iloc[4:5, 3] = df1.iloc[4:5, 3].apply(lambda x: f'{x:.0%}')
st.dataframe(df1, hide_index=True)
st.markdown(' ### ')

# TABLE 2
df2 = load_excel_data(excel_file, sheet_name, 'F:K', 19, 1)
df2 = df2.fillna('')
st.dataframe(df2, hide_index=True)

st.header('Bull/Bear Ratios')
st.image('fig1_05_07_2024.png', caption='Figure 1', use_column_width=True)

st.header('Put/Call & Vix')
st.image('fig2_05_07_2024.png', caption='Figure 2', use_column_width=True)



import yfinance as yf
import matplotlib.pyplot as plt

# Fetch data
@st.cache_data
def fetch_data(ticker, start):
    return yf.download(ticker, start=start)['Adj Close']

sp500 = fetch_data('^GSPC', '2021-11-01')
russell2000 = fetch_data('^RUT', '2021-11-01')
treasury_yield = fetch_data('^TNX', '2021-11-01')

# Calculate daily returns
sp500_returns = sp500.pct_change().dropna()
russell2000_returns = russell2000.pct_change().dropna()
treasury_yield_returns = treasury_yield.pct_change().dropna()

# Calculate rolling 42-day (2-month) correlations
rolling_corr_sp500 = sp500_returns.rolling(window=44).corr(treasury_yield_returns)
rolling_corr_russell2000 = russell2000_returns.rolling(window=42).corr(treasury_yield_returns)

# Get the current 2-month rolling correlations
current_rolling_corr_sp500 = rolling_corr_sp500.iloc[-1]
current_rolling_corr_russell2000 = rolling_corr_russell2000.iloc[-1]
current_date = rolling_corr_sp500.index[-1]

# Plot the rolling correlations over time
fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(rolling_corr_sp500, label='S&P 500 vs. 10-Yr. Yield')
ax.plot(rolling_corr_russell2000, label='Russell 2000 vs. 10-Yr. Yield', color='orange')
ax.set_title('Rolling 2-Month Correlation')
ax.set_xlabel('Date')
ax.set_ylabel('Correlation')
ax.legend()
st.pyplot(fig)


st.image('fig33.jpeg', caption='Figure 3', use_column_width=True)
