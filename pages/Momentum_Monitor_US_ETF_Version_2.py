import pandas as pd
import streamlit as st

st.set_page_config(page_title='US ETF Momentum',
                   page_icon=':bar_chart:',
                   layout="wide")

#st.header('Momentum Monitor India ETF')
st.markdown("<div style='text-align: center;'> <h1>Momentum Monitor US ETF</h1> </div>", unsafe_allow_html=True)

excel_file = 'US_ETF_MOMENTUM.xlsx'
sheet_name = 'Aset class Rankings'


# Function to apply color based on cell value
def color_cells(val):
    color = '#ffcccc' if val == 'CASH' else ('#ccffcc' if val == 'INVESTED' else '')
    return f'background-color: {color}'

def percent_one_decimal(val):
    return "{:.1f}%".format(val * 100)

def percent_whole_number(val):
    return "{:.0f}%".format(val * 100)


images_col = {"Images": [
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
    ]
}

df_images = pd.DataFrame(images_col)
aa = df_images['Images']

# TABLE 1
df1 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='D:J',
                   header=5,
                   nrows=33)

df1 = df1.rename(columns={'Unnamed: 3' : 'TICKER'})
df1 = df1.rename(columns={'Unnamed: 4' : 'ETF'})
df1 = df1.rename(columns={'Unnamed: 5' : 'Relative Ranking'})
df1 = df1.drop(['Unnamed: 6'], axis=1)
df1.insert(3, "Relative Ranking.1", aa)
df1 = df1.style.applymap(color_cells, subset=['Above 30 D ', 'Above 60 D', 'Above 200D'])
st.markdown("<div style='text-align: center;'> <h2>Relative Ranking</h2> </div>", unsafe_allow_html=True)
df1_html = df1.to_html(escape=False)

# CSS to center table content and modify text size
style = """
<style>
    th, td {
        text-align: center;
        font-size: 15px; /* Example size, adjust as needed */
    }
    table {
        margin-left: auto;
        margin-right: auto;
    }
</style>
"""

# Combine the style with the DataFrame HTML
df1_html = style + df1_html
st.markdown(df1_html, unsafe_allow_html=True)
st.markdown('## ')




images_col1 = {"Images": [
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
    ]
}

df_images1 = pd.DataFrame(images_col1)
bb = df_images1['Images']

# TABLE 2
df2 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='D:P',
                   header=42,
                   nrows=33)

df2 = df2.rename(columns={'Unnamed: 3' : 'TICKER'})
df2 = df2.rename(columns={'Unnamed: 4' : 'ETF'})
df2 = df2.rename(columns={'Clsoeness to 52 week' : 'Closeness to 52 week.1'})
df2 = df2.rename(columns={'median' : 'Median'})
relative_ranking = df2['Relative ranking']
df2 = df2.drop(['Relative ranking'], axis=1)
df2 = df2.drop(['Unnamed: 9'], axis=1)
df2.insert(2, "Relative Ranking", bb)
df2 = df2.style.format({
      'U/D': percent_one_decimal, 
      'Breadth': percent_whole_number, 
      'Closeness to 52 week': percent_one_decimal,
      '3 month return': '{:.1f}',
      'Median': '{:.1f}'
})
st.markdown("<div style='text-align: center;'> <h2>Equity Ranking: Momentum + Breadth + Upgrades</h2> </div>", unsafe_allow_html=True)
df2_html = df2.to_html(escape=False)
st.markdown(df2_html, unsafe_allow_html=True)
st.markdown('## ')




# TABLE 3
df3 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='D:G',
                   header=80,
                   nrows=33)

df3 = df3.style.format({'Upgrades 1 month': percent_one_decimal, 'Downgrades 1 month': percent_one_decimal})
st.markdown("<div style='text-align: center;'> <h2>Equity ETF - Upgrades</h2> </div>", unsafe_allow_html=True)
df3_html = df3.to_html(escape=False)
st.markdown(df3_html, unsafe_allow_html=True)
st.markdown('## ')



