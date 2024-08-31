import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title='Indian Companies Result', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('Indian Companies Result')

# Define the URL
url = "https://indian-results.streamlit.app/"

# Create a clickable link
st.markdown(f'Link to [Indian Companies Result]({url})')
