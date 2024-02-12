import pandas as pd
import streamlit as st

st.set_page_config(page_title='India ETF Momentum',
                   page_icon=':bar_chart:')

#st.header('Momentum Monitor India ETF')
st.markdown("<div style='text-align: center;'> <h1>Momentum Monitor India ETF</h1> </div>", unsafe_allow_html=True)

excel_file = 'INDIA_ETF_MOMENTUM.xlsx'
sheet_name = 'Aset class Rankings'


# Function to apply color based on cell value
def color_cells(val):
    color = '#ffcccc' if val == 'CASH' else ('#ccffcc' if val == 'INVESTED' else '')
    return f'background-color: {color}'

def color_cells_1(val):
    color = '#ffcccc' if val >= 5 else ('#ccffcc' if val <=2 else '#ffffcc')
    return f'background-color: {color}'

def color_cells_2(val):
    color = '#ffcccc' if val >= 4 else ('#ccffcc' if val < 0 else '#ffffcc')
    return f'background-color: {color}'

def percent_one_decimal(val):
    return "{:.1f}%".format(val * 100)

def percent_whole_number(val):
    return "{:.0f}%".format(val * 100)


images_col = {"Images": [
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
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
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
    ]
}

df_images = pd.DataFrame(images_col)
aa = df_images['Images']

# TABLE 1
df1 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='D:J',
                   header=5,
                   nrows=14)

df1 = df1.rename(columns={'Unnamed: 3' : 'TICKER'})
df1 = df1.rename(columns={'Unnamed: 4' : 'ETF'})
df1 = df1.rename(columns={'Unnamed: 5' : 'Relative Ranking'})
df1 = df1.drop(['Unnamed: 6'], axis=1)
df1.insert(3, "Images", aa)
df1 = df1.style.applymap(color_cells, subset=['Above 30 D ', 'Above 60 D', 'Above 200D'])
#st.markdown('### Relative Ranking')
# Center the title using HTML and CSS within st.markdown
st.markdown("<div style='text-align: center;'> <h2>Relative Ranking</h2> </div>", unsafe_allow_html=True)
#st.dataframe(df1, hide_index=True)
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
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
    ]
}

df_images1 = pd.DataFrame(images_col1)
bb = df_images1['Images']

# TABLE 2
df2 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='D:P',
                   header=23,
                   nrows=14)

df2 = df2.rename(columns={'Unnamed: 3' : 'TICKER'})
df2 = df2.rename(columns={'Unnamed: 4' : 'ETF'})
df2 = df2.rename(columns={'Clsoeness to 52 week' : 'Closeness to 52 week.1'})
relative_ranking = df2['Relative ranking']
df2 = df2.drop(['Relative ranking'], axis=1)
df2 = df2.drop(['Unnamed: 9'], axis=1)
#df2.insert(2, "Relative Ranking", relative_ranking)
df2.insert(2, "Relative Ranking", bb)
df2 = df2.style.format({
      'U/D': percent_one_decimal, 
      'Breadth': percent_whole_number, 
      'Closeness to 52 week': percent_one_decimal,
      '3 month return': '{:.1f}',
      'median': '{:.1f}'
})
#st.markdown('### Equity Ranking: Momentum + Breadth + Upgrades')
# Center the title using HTML and CSS within st.markdown
st.markdown("<div style='text-align: center;'> <h2>Equity Ranking: Momentum + Breadth + Upgrades</h2> </div>", unsafe_allow_html=True)
#st.dataframe(df2, hide_index=True)
df2_html = df2.to_html(escape=False)
st.markdown(df2_html, unsafe_allow_html=True)
st.markdown('## ')


# TABLE 3
df3 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='D:I',
                   header=42,
                   nrows=14)

df3 = df3.drop(['Unnamed: 5'], axis=1)
df3 = df3.style.applymap(color_cells)
#st.markdown('### Equity ETF - MA Signals')
st.markdown("<div style='text-align: center;'> <h2>Equity ETF - MA Signals</h2> </div>", unsafe_allow_html=True)
#st.dataframe(df3, hide_index=True)
df3_html = df3.to_html(escape=False)
st.markdown(df3_html, unsafe_allow_html=True)
st.markdown('## ')



# TABLE 4
df4 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='K:N',
                   header=42,
                   nrows=14)

df4 = df4.rename(columns={'TICKER.1' : 'TICKER'})
df4 = df4.rename(columns={'ETF.1' : 'ETF'})
df4 = df4.style.format({'Upgrades 1 month': percent_one_decimal, 'Downgrades 1 month': percent_one_decimal})
#st.markdown('### Equity ETF - Upgrades')
st.markdown("<div style='text-align: center;'> <h2>Equity ETF - Upgrades</h2> </div>", unsafe_allow_html=True)
#st.dataframe(df4, hide_index=True)
df4_html = df4.to_html(escape=False)
st.markdown(df4_html, unsafe_allow_html=True)
st.markdown('## ')
