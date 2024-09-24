import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title='Investment Diversification Heat Map', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('Investment Diversification Heat Map')

# Define the URL
url = "https://ai.gopubby.com/how-to-create-the-investment-diversification-heat-map-in-python-c72b7fd91c57"

# Create a clickable link
st.markdown(f'Link to [How to Create the Investment Diversification Heat Map in Python]({url})')

st.write('Portfolio is 60% SPY and 40% AIRR')

st.write('''
            For the calculation of the portfolio return:
         
            Portfolio = SPY x 0.6 + AIRR x 0.40
         
            Example for Year 2015:
         
            Portfolio = SPY(1.23%) * 0.6 + AIRR(-9.51%) * 0.4
         
            Portfolio = -3.06%
         ''')

st.image('Figure_1.png', caption='Figure 1', use_column_width=True)
st.image('Figure_2.png', caption='Figure 2', use_column_width=True)
