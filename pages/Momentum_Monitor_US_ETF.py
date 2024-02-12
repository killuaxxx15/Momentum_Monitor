import pandas as pd
import streamlit as st

st.set_page_config(page_title='US ETF Momentum Monitor',
                   page_icon=':bar_chart:')

st.header('Momentum Monitor US ETF')

excel_file = 'sample.xlsx'
sheet_name = 'Aset class Rankings'


images_col = {"Images": [
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/blue_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/blue_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/blue_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
    ]
}

df_images = pd.DataFrame(images_col)
#aa = df_images['Images']
#aa = aa.to_html(escape=False)
#st.markdown(aa, unsafe_allow_html=True)
df_images_html = df_images.to_html(escape=False)
#st.markdown(df_images_html, unsafe_allow_html=True)
#st.markdown('## ')

aa = df_images['Images']

df2 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:J',
                   header=13,
                   nrows=11)

df2 = df2.rename(columns={'Unnamed: 4' : 'ETF'})
df2 = df2.rename(columns={'Unnamed: 5' : 'Relative Ranking'})
df2 = df2.drop(['Unnamed: 6'], axis=1)
df2.insert(2, "Images", aa)
st.markdown('### Table 2: Relative Ranking')
#st.dataframe(df2, hide_index=True)

df2_html = df2.to_html(escape=False)
st.markdown(df2_html, unsafe_allow_html=True)
st.markdown('## ')






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
#st.markdown(df_html, unsafe_allow_html=True)






