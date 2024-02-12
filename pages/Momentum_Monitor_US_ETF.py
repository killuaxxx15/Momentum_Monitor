import pandas as pd
import streamlit as st

st.set_page_config(page_title='US ETF Momentum Monitor',
                   page_icon=':bar_chart:')

st.header('Momentum Monitor US ETF')

excel_file = 'sample.xlsx'
sheet_name = 'Aset class Rankings'

def color_cells(val):
    color = '#ffcccc' if val == 'CASH' else ('#ccffcc' if val == 'INVESTED' else '')
    return f'background-color: {color}'

def color_cells_1(val):
    color = '#ffcccc' if val >= 5 else ('#ccffcc' if val <=2 else '#ffffcc')
    return f'background-color: {color}'

def color_cells_2(val):
    color = '#ffcccc' if val > 2 else ('#ccffcc' if val < 0 else '#ffffcc')
    return f'background-color: {color}'

def percent_one_decimal(val):
    return "{:.1f}%".format(val * 100)

def percent_whole_number(val):
    return "{:.0f}%".format(val * 100)



images_col = {"Images": [
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
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

df2 = df2.style.applymap(color_cells, subset=['Above 30 D ', 'Above 60 D', 'Above 200D'])

df2_html = df2.to_html(escape=False)
st.markdown(df2_html, unsafe_allow_html=True)
st.markdown('## ')







images_col1 = {"Images": [
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/red_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/green_circle.png" width="20" height="20">',
        '<img src="https://raw.githubusercontent.com/killuaxxx15/google_trends/main/yellow_circle.png" width="20" height="20">',
    ]
}

df_images1 = pd.DataFrame(images_col1)
bb = df_images1['Images']

# TABLE 3
df3 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:P',
                   header=28,
                   nrows=9)

df3 = df3.rename(columns={'Unnamed: 5' : 'U/D'})
df3 = df3.rename(columns={'Unnamed: 6' : 'Breadth'})
df3 = df3.rename(columns={'Unnamed: 7' : 'Closeness to 52 week'})
df3 = df3.rename(columns={'Unnamed: 8' : '3 month return'})
df3 = df3.rename(columns={'Unnamed: 10' : 'U/D.1'})
df3 = df3.rename(columns={'Unnamed: 11' : 'Breadth.1'})
df3 = df3.rename(columns={'Unnamed: 12' : 'Closeness to 52 week.1'})
df3 = df3.rename(columns={'Unnamed: 13' : '3 month return.1'})
df3 = df3.rename(columns={'Unnamed: 14' : 'Median'})
df3 = df3.rename(columns={'Unnamed: 15' : 'Relative Ranking'})
relative_ranking = df3['Relative Ranking']
df3 = df3.drop(['Relative Ranking'], axis=1)
df3 = df3.drop(['Unnamed: 9'], axis=1)
df3.insert(1, "Relative Ranking", bb)
df3 = df3.style.format({
      'U/D': percent_one_decimal, 
      'Breadth': percent_whole_number, 
      'Closeness to 52 week': percent_one_decimal,
      '3 month return': '{:.1f}',
      'Median': '{:.1f}',
})
st.markdown('### Table 3: Equity Ranking: Momentum + Breadth + Upgrades')
#st.dataframe(df3, hide_index=True)
df3_html = df3.to_html(escape=False)
st.markdown(df3_html, unsafe_allow_html=True)



