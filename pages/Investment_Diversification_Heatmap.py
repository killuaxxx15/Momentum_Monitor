import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title='Investment Diversification Heat Map', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('Investment Diversification Heat Map')
st.header('To be edited')

# Define the URL
url = "https://ai.gopubby.com/how-to-create-the-investment-diversification-heat-map-in-python-c72b7fd91c57"

# Create a clickable link
st.markdown(f'Link to [How to Create the Investment Diversification Heat Map in Python]({url})')

st.subheader('Sectors')
st.image('Figure_1.png', caption='SECTORS', use_column_width=True)

st.subheader('Countries')
st.image('Figure_2.png', caption='COUNTRIES', use_column_width=True)
