import pandas as pd
import streamlit as st

st.set_page_config(page_title='Global Momentum',
                   page_icon=':bar_chart:')

st.header('To be edited')

excel_file = 'sample.xlsx'
sheet_name = 'Aset class Rankings'



# Function to apply color based on cell value
def color_cells(val):
    color = '#ffcccc' if val == 'CASH' else ('#ccffcc' if val == 'INVESTED' else '')
    return f'background-color: {color}'

# Function to format as whole number percentage
def format_percentage_whole(val):
    if isinstance(val, (int, float)):
        return '{:.0%}'.format(val)
    return val

# Function to format as percentage with at most 1 decimal place
def format_percentage_one_decimal(val):
    if isinstance(val, (int, float)):
        return '{:.1%}'.format(val)
    return val



df1 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:H',
                   header=2,
                   nrows=5)

# Applying the styling to the DataFrame
df1 = df1.style.applymap(color_cells)
st.markdown('#### Table 1: Equity Relative to other Asset Classes')
st.dataframe(df1, hide_index=True)



df2 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:J',
                   header=11,
                   nrows=13)

# Apply the styling
styled_df = df2.style.applymap(color_cells)

# Convert styled DataFrame to HTML without including the index
df_html = styled_df.to_html(escape=False, index=False)

# Display the HTML in Streamlit
st.markdown('#### Table 2: Relative Ranking', unsafe_allow_html=True)
st.markdown(df_html, unsafe_allow_html=True)
st.markdown('#### ')





df3 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:P',
                   header=27,
                   nrows=10)

# Apply the formatting to the specific columns
df3['Breadth'] = df3['Breadth'].apply(format_percentage_whole)
df3['Closeness to 52 week'] = df3['Closeness to 52 week'].apply(format_percentage_one_decimal)
df3['U/D'] = df3['U/D'].apply(format_percentage_one_decimal)
st.markdown('#### Table 3: Equity Ranking: Momentum + Breadth + Upgrades')
st.dataframe(df3, hide_index=True)



df4 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:I',
                   header=40,
                   nrows=9)

df4 = df4.style.applymap(color_cells)
st.markdown('#### Table 4: Equity ETF - MA Signals')
st.dataframe(df4, hide_index=True)


df5 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='K:M',
                   header=40,
                   nrows=10)

st.markdown('#### Table 5: Equity ETF - Upgrades')
df5['Upgrades 1 month'] = df5['Upgrades 1 month'].apply(format_percentage_one_decimal)
df5['Downgrades 1 month'] = df5['Downgrades 1 month'].apply(format_percentage_one_decimal)
st.dataframe(df5, hide_index=True)


df6 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:F',
                   header=52,
                   nrows=6)

column_index1 = 1
df6.iloc[0:6, column_index1] = df6.iloc[0:6, column_index1].apply(format_percentage_one_decimal)
st.markdown('#### Table 6: Long Term Forecasts (above local rates)')
st.dataframe(df6, hide_index=True)









def value_to_circle(value):
    # Check if value is NaN or not a number (int or float)
    if pd.isna(value) or not isinstance(value, (int, float)):
        return ''  # or some default representation

    if value <= 2:
        color = 'green'
    elif 3 <= value <= 4:
        color = 'yellow'
    else:
        color = 'red'

    return f'<span style="color: {color}; font-size: 20px;">●</span>'

df20 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:J',
                   header=11,
                   nrows=13)

# Replace None/NaN values with an empty string
df20 = df20.fillna('')

# Convert rows 4 to 14 of the 3rd column to integers
column_index1 = 1  # Index for the '3 month return' column
column_index2 = 2  # Index for the '6 month rank' column
df20.iloc[2:13, column_index1] = df20.iloc[2:13, column_index1].apply(lambda x: int(x) if pd.notna(x) else x)

# Apply the value_to_circle function to the 3rd column
df20.iloc[2:13, column_index2] = df20.iloc[2:13, column_index2].apply(value_to_circle)

# Applying the styling to the DataFrame
df20_styled = df20.style.applymap(color_cells)

def format_as_percent(value):
    # Check if the value is a number and not NaN
    if pd.notna(value) and isinstance(value, (int, float)):
        # Convert decimal to percentage, round to nearest whole number, and append percent symbol
        return f"{round(value * 100)}%"
    return value  # Return the value unchanged if it's not a number

# Apply the format_as_percent function to the first three columns of the first row
for col in range(3):  # Loop over the first three columns
    df20.iloc[0, col] = format_as_percent(df20.iloc[0, col])

# Display in Streamlit
st.markdown('#### Table 2 Ver 2 with colored circles')
st.markdown(df20_styled.to_html(escape=False), unsafe_allow_html=True)
