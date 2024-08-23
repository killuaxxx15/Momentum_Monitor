import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title='Data Screener', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('Data Screener')

# Define the URL
url = "https://data-screener.streamlit.app"

# Create a clickable link
st.markdown(f'#Link: [Data Screener]({url})')
