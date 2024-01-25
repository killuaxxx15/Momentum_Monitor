import pandas as pd
import pytrends
from pytrends.request import TrendReq
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

pytrend = TrendReq(hl='en-US', tz=360)

st.header('Google Trends Keyword Search')

keyword = st.text_input("Enter a keyword", help="Look up on Google Trends")

# Timeframe options
TIMEFRAME_OPTIONS = {
    '2004 to present': 'all',
    'Past 5 years': 'today 5-y',
    'Past 12 months': 'today 12-m',
    'Past 90 days': 'today 3-m',
    'Past 7 days': 'now 7-d',
    'Past day': 'now 1-d',
    'Past 4 hours': 'now 4-H',
    'Past hour': 'now 1-H'
}

# Selecting the index for 'Past 5 years'
default_timeframe_index = list(TIMEFRAME_OPTIONS.keys()).index('Past 5 years')
timeframe = st.selectbox("Select Timeframe", list(TIMEFRAME_OPTIONS.keys()), index=default_timeframe_index)

# Updated country list with 'Worldwide' option
COUNTRY = ['Worldwide', 'US', 'PH', 'IN', 'CN', 'TH', 'VN', 'GB', 'KR', 'JP', 'RU', 'AE']
country = st.selectbox("Choose a country or worldwide", COUNTRY, index=COUNTRY.index("US"))

# Updated get_data function to handle 'Worldwide'
def get_data(keyword, country, timeframe):
    KEYWORDS = [keyword]
    KEYWORDS_CODES = [pytrend.suggestions(keyword=i)[0] for i in KEYWORDS]
    df_CODES = pd.DataFrame(KEYWORDS_CODES)
    # st.dataframe(df_CODES)

    EXACT_KEYWORDS = df_CODES['mid'].to_list()
    CATEGORY = 0
    SEARCH_TYPE = ''

    # Set geo parameter to '' for worldwide
    geo_param = '' if country == 'Worldwide' else country

    pytrend.build_payload(kw_list=EXACT_KEYWORDS,
                          timeframe=TIMEFRAME_OPTIONS[timeframe],
                          geo=geo_param,
                          cat=CATEGORY,
                          gprop=SEARCH_TYPE)
    df_trends = pytrend.interest_over_time()

    df_trends = df_trends.drop('isPartial', axis=1)  # drop "isPartial"
    df_trends.reset_index(level=0, inplace=True)  # reset_index
    df_trends.columns = ['Date', country]  # change column names

    return df_trends

# Matplotlib function for plotting
def linePlot(input_data, keyword, country):
    plt.figure(figsize=(10, 4))
    plt.plot(input_data['Date'], input_data[country])
    plt.title(f'Google Trends for "{keyword}" in {country}')
    plt.xlabel('Date')
    plt.ylabel('Trends Index')
    plt.grid(True)
    plt.xticks(rotation=45)  # Rotate date labels for better readability
    st.pyplot(plt)

if keyword and country:
    df_trends = get_data(keyword, country, timeframe)
    st.dataframe(df_trends, 2000, 200)
    linePlot(df_trends, keyword, country)  # Updated function call
