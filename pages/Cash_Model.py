import pandas as pd
import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title='Cash Model', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('Cash Model')

# Display the last update date
st.markdown('#### Updated: 19/07/2024')

# Define Excel file and sheet name variables
excel_file = 'Cash_model_19_07_2024.xlsx'
sheet_name = 'Sheet1'


# Cache data loading function for better performance
@st.cache_data
def load_excel_data(file_name, sheet, use_columns, header_row, num_rows):
    return pd.read_excel(file_name, sheet_name=sheet, usecols=use_columns, header=header_row, nrows=num_rows)

# Define a function to format numbers
def format_number(val):
    if pd.isna(val) or val == '':
        return ''
    try:
        val = float(val)
        if val.is_integer():
            return "{:.0f}".format(val)
        else:
            return "{:.2f}".format(val)
    except ValueError:
        return val


# TABLE 1
df1 = load_excel_data(excel_file, sheet_name, 'C:H', 7, 9)
df1 = df1.fillna('')
df1 = df1.applymap(format_number)
st.markdown('### Table 1')
st.dataframe(df1, hide_index=True)

# TABLE 2
df2 = load_excel_data(excel_file, sheet_name, 'C:E', 19, 1)
st.markdown('### Table 2')
st.dataframe(df2, hide_index=True)





import yfinance as yf
import matplotlib.pyplot as plt

# Set up the Streamlit app
st.markdown("### Breadth")
st.markdown("#### Rolling 252-day Correlation between SPY and RSP")

# Fetch data
@st.cache_data
def fetch_data(ticker, start):
    return yf.download(ticker, start=start)['Adj Close']

spy = fetch_data('SPY', '2003-01-01')
rsp = fetch_data('RSP', '2003-01-01')

# Calculate daily returns
spy_returns = spy.pct_change().dropna()
rsp_returns = rsp.pct_change().dropna()

# Calculate rolling 252-day correlation
rolling_corr = spy_returns.rolling(window=252).corr(rsp_returns)

# Find the minimum rolling correlation
min_rolling_corr = rolling_corr.min()
min_rolling_corr_date = rolling_corr.idxmin()

# Get the current 252-day rolling correlation
current_rolling_corr = rolling_corr.iloc[-1]
current_rolling_corr_date = rolling_corr.index[-1]

# Display the results
#st.write(f"The lowest 252-day rolling correlation is {min_rolling_corr:.4f} on {min_rolling_corr_date.date()}")

# Plot the rolling correlation over time, highlighting the lowest correlation
#fig1, ax1 = plt.subplots(figsize=(14, 7))
#ax1.plot(rolling_corr, label='252-day Rolling Correlation')
#ax1.axhline(y=min_rolling_corr, color='r', linestyle='--', label=f'Lowest Correlation: {min_rolling_corr:.4f}')
#ax1.set_title('252-day Rolling Correlation between SPY and RSP (Highlighting Lowest)')
#ax1.set_xlabel('Date')
#ax1.set_ylabel('Correlation')
#ax1.legend()
#st.pyplot(fig1)

st.write(f"The current 252-day rolling correlation is {current_rolling_corr:.4f} on {current_rolling_corr_date.date()}")
# Plot the rolling correlation over time, highlighting the current correlation
fig2, ax2 = plt.subplots(figsize=(14, 7))
ax2.plot(rolling_corr, label='252-day Rolling Correlation')
ax2.axhline(y=current_rolling_corr, color='g', linestyle='--', label=f'Current Correlation: {current_rolling_corr:.4f}')
ax2.set_title('252-day Rolling Correlation between SPY and RSP')
ax2.set_xlabel('Date')
ax2.set_ylabel('Correlation')
ax2.legend()
st.pyplot(fig2)


