import pandas as pd
import streamlit as st

st.set_page_config(page_title='Global Momentum',
                   page_icon=':bar_chart:',
                   layout='wide')

excel_file = 'sample.xlsx'
sheet_name = 'Aset class Rankings'

col1, col2 = st.columns(2)

df1 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:H',
                   header=5,
                   nrows=6)

# Function to apply color based on cell value
def color_cells(val):
    color = '#ffcccc' if val == 'CASH' else ('#ccffcc' if val == 'INVESTED' else '')
    return f'background-color: {color}'

# Applying the styling to the DataFrame
df1 = df1.style.applymap(color_cells)

# Display the table with styling but without index
#col1.markdown('### Table 1')
#col1.dataframe(df1, hide_index=True)



df2 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:J',
                   header=13,
                   nrows=14)

col2.markdown('### Table 2 Ver 1 as dataframe')

# Replace None/NaN values with an empty string for all columns except the ones to be converted to integers
columns_to_int = ['3 month return', '6 month rank']
for col in df2.columns:
    if col not in columns_to_int:
        df2[col] = df2[col].fillna('')

# Convert '3 month return' and '6 month rank' to integers
# First replace NaN with 0 or any other default integer value
df2['3 month return'] = df2['3 month return'].fillna(0).round().astype(int)
df2['6 month rank'] = df2['6 month rank'].fillna(0).round().astype(int)

# Applying the styling to the DataFrame
# Ensure that color_cells function can handle integer formatting
df2 = df2.style.applymap(color_cells)
col2.dataframe(df2, hide_index=True)




df3 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:O',
                   header=29,
                   nrows=10)

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

# Apply the formatting to the specific columns
df3['Breadth'] = df3['Breadth'].apply(format_percentage_whole)
df3['Closeness to 52 week'] = df3['Closeness to 52 week'].apply(format_percentage_one_decimal)
df3['U/D'] = df3['U/D'].apply(format_percentage_one_decimal)


# Define the yellow background styling function
def yellow_background(val):
    return 'background-color: yellow'

# Custom formatting function
def custom_format(val):
    if isinstance(val, float):
        return f"{val:.1f}" if val != int(val) else f"{int(val)}"
    return val

# Apply styling and custom formatting to the DataFrame
df3 = df3.style.applymap(yellow_background, subset=['median']).format({
    '3 month return': '{:.1f}',  # Format '3 month return' with 1 decimal place
    'median': custom_format  # Apply custom formatting to 'median' column
})

#col1.markdown('### ')
col1.markdown('### Table 3 Equity - Momentum + Breadth + Uptrades')
col1.dataframe(df3, hide_index=True)

col3, col4, col5 = st.columns(3)

col4.markdown('### Table 1')
col4.dataframe(df1, hide_index=True)

df4 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='D:H',
                   header=41,
                   nrows=9)

col5.markdown('### Table 4')
# Applying the styling to the DataFrame
df4 = df4.style.applymap(color_cells)
col5.dataframe(df4, hide_index=True)


df5 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='J:L',
                   header=41,
                   nrows=11)

col3.markdown('### Table 5')
df5['Upgrades 1 month'] = df5['Upgrades 1 month'].apply(format_percentage_one_decimal)
df5['Downgrades 1 month'] = df5['Downgrades 1 month'].apply(format_percentage_one_decimal)
col3.dataframe(df5, hide_index=True)




df6 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='D:E',
                   header=55,
                   nrows=6)

column_index3 = 1
df6.iloc[0:6, column_index3] = df6.iloc[0:6, column_index3].apply(format_percentage_one_decimal)
col4.markdown('### Long term Forecasts')
col4.dataframe(df6, hide_index=True)







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
                   header=13,
                   nrows=14)

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
st.markdown('### Table 2 Ver 2 with colored circles')
st.write(df20_styled.to_html(escape=False), unsafe_allow_html=True)



