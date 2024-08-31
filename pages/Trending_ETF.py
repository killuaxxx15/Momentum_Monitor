import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title='Trending ETF Trend', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('Trending ETF Trend')

# Display the last update date
st.markdown('#### Updated: 31/08/2024')

st.image('stock_screener_2.jpg', caption='ETF Price Trend with Logarithmic Regression', use_column_width=True)

# Define the URL
url = "https://medium.com/tech-talk-tank/everyone-can-visualize-stock-data-with-these-python-codes-46be14fca954"

# Create a clickable link
st.markdown(f'Link to the [Medium article]({url})')
