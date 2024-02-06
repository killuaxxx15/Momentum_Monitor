import pandas as pd
import streamlit as st

st.set_page_config(page_title='Global Momentum',
                   page_icon=':bar_chart:')

st.header('Global Momentum Dashboard')

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

df2 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:J',
                   header=13,
                   nrows=11)

# Replace None/NaN values with an empty string
df2 = df2.fillna('')

# Convert rows 4 to 14 of the 3rd column to integers
column_index1 = 1  # Index for the '3 month return' column
column_index2 = 2  # Index for the '6 month rank' column
#df2.iloc[2:13, column_index1] = df2.iloc[2:13, column_index1].apply(lambda x: int(x) if pd.notna(x) else x)
df2.iloc[0:11, column_index1] = df2.iloc[0:11, column_index1].apply(lambda x: int(x) if pd.notna(x) else x)
# Apply the value_to_circle function to the 3rd column
#df2.iloc[2:13, column_index2] = df2.iloc[2:13, column_index2].apply(value_to_circle)
df2.iloc[0:11, column_index2] = df2.iloc[0:11, column_index2].apply(value_to_circle)

# Applying the styling to the DataFrame
df2_styled = df2.style.applymap(color_cells)

def format_as_percent(value):
    # Check if the value is a number and not NaN
    if pd.notna(value) and isinstance(value, (int, float)):
        # Convert decimal to percentage, round to nearest whole number, and append percent symbol
        return f"{round(value * 100)}%"
    return value  # Return the value unchanged if it's not a number

# Apply the format_as_percent function to the first three columns of the first row
#for col in range(3):  # Loop over the first three columns
#    df2.iloc[0, col] = format_as_percent(df2.iloc[0, col])

st.write(df2_styled.columns)

# Display in Streamlit
df2_styled = df2_styled.rename(columns={'Unnamed: 5' : 'Relative Ranking'})
st.markdown('#### Table 2: Relative Ranking')
st.markdown(df2_styled.to_html(escape=False), unsafe_allow_html=True)
st.markdown('#### ')




def color_cells_2(val):
    # Check if val is NaN or not a numeric value
    if pd.isna(val) or not isinstance(val, (int, float)):
        return ''
    if val < 0:
        return 'background-color: #ccffcc'
    elif 0 <= val <= 2:
        return 'background-color: lightyellow'
    else:  # val > 2
        return 'background-color: #ffcccc'
  
df3 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:P',
                   header=27,
                   #skiprows=2,
                   nrows=10)

df3 = df3.fillna('')
# Apply the formatting to the specific columns
df3['Breadth'] = df3['Breadth'].apply(format_percentage_whole)
df3['Closeness to 52 week'] = df3['Closeness to 52 week'].apply(format_percentage_one_decimal)
df3['U/D'] = df3['U/D'].apply(format_percentage_one_decimal)
df3['3 month return'] = pd.to_numeric(df3['3 month return'])
df3['3 month return'] = df3['3 month return'].round(1)
relative_ranking = df3['Relative ranking']
df3 = df3.drop(['Relative ranking'], axis=1)
df3.insert(1, "Relative Ranking", relative_ranking)
# Apply the styling function to the 'Relative ranking' column of the DataFrame
#df3 = df3.style.applymap(color_cells_2, subset=['Relative Ranking'])
df3 = df3.fillna('')
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
#df6.iloc[0:6, column_index1] = df6.iloc[0:6, column_index1].apply(format_percentage_one_decimal)
df6.iloc[0:6, column_index1] = df6.iloc[0:6, column_index1].apply(lambda x: format_percentage_one_decimal(x) if pd.notnull(x) else '')
st.markdown('#### Table 6: Long Term Forecasts (above local rates)')
st.dataframe(df6, hide_index=True)
