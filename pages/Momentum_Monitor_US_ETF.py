import pandas as pd
import streamlit as st

st.set_page_config(page_title='US ETF Momentum Monitor',
                   page_icon=':bar_chart:')

st.header('Momentum Monitor US ETF')

# Replace these URLs with the raw URLs of your images in the GitHub repository
data = {
    "Name": ["Image 1", "Image 2"],
    "Image": [
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/user_avatar.png" width="50" height="50">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/ai_bot_avatar.png" width="50" height="50">',
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert the DataFrame to HTML and allow column names to be displayed
df_html = df.to_html(escape=False)

# Display the DataFrame as HTML in Streamlit
st.markdown(df_html, unsafe_allow_html=True)
