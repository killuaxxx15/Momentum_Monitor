import pandas as pd
import pytrends
from pytrends.request import TrendReq
import streamlit as st
import matplotlib.pyplot as plt
from pytrends import exceptions

st.header('Google Trends Keyword Search')

pytrend = TrendReq(hl='en-US', tz=360)

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

default_timeframe_index = list(TIMEFRAME_OPTIONS.keys()).index('Past 12 months')
timeframe = st.selectbox("Select Timeframe", list(TIMEFRAME_OPTIONS.keys()), index=default_timeframe_index)

COUNTRY = ['Worldwide', 'US', 'PH', 'CN', 'IN', 'GB', 'KR', 'JP', 'TH', 'VN', 'RU', 'AE']
country = st.selectbox("Choose a country or worldwide", COUNTRY, index=COUNTRY.index("US"))

def get_data(keyword, country, timeframe):
    KEYWORDS = [keyword]
    KEYWORDS_CODES = [pytrend.suggestions(keyword=i)[0] for i in KEYWORDS]
    df_CODES = pd.DataFrame(KEYWORDS_CODES)
    st.dataframe(df_CODES)

    EXACT_KEYWORDS = df_CODES['mid'].to_list()
    CATEGORY = 0
    SEARCH_TYPE = ''

    geo_param = '' if country == 'Worldwide' else country

    try:
        pytrend.build_payload(kw_list=EXACT_KEYWORDS,
                              timeframe=TIMEFRAME_OPTIONS[timeframe],
                              geo=geo_param,
                              cat=CATEGORY,
                              gprop=SEARCH_TYPE)
        df_trends = pytrend.interest_over_time()
    except exceptions.TooManyRequestsError:
        st.error("Too many requests sent to Google Trends. Please reduce the timeframe or try again later.")
        return pd.DataFrame()  # Return an empty DataFrame

    df_trends = df_trends.drop('isPartial', axis=1)
    df_trends.reset_index(level=0, inplace=True)
    df_trends.columns = ['Date', country]

    return df_trends

def linePlot(input_data, keyword, country):
    if not input_data.empty:
        plt.figure(figsize=(10, 4))
        plt.plot(input_data['Date'], input_data[country])
        plt.title(f'Google Trends for "{keyword}" in {country}')
        plt.xlabel('Date')
        plt.ylabel('Trends Index')
        plt.grid(True)
        plt.xticks(rotation=45)
        st.pyplot(plt)

if keyword and country:
    df_trends = get_data(keyword, country, timeframe)
    if not df_trends.empty:
        # st.dataframe(df_trends, 2000, 200)
        linePlot(df_trends, keyword, country)
