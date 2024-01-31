import pandas as pd
import streamlit as st

st.set_page_config(page_title='Global Momentum',
                   page_icon=':bar_chart:',
                   layout='wide')

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

# Define the yellow background styling function
def yellow_background(val):
    return 'background-color: yellow'

# Custom formatting function
def custom_format(val):
    if isinstance(val, float):
        return f"{val:.1f}" if val != int(val) else f"{int(val)}"
    return val

# Function to read data from Excel and apply styling
def read_excel_and_style(sheet_name, usecols, header, nrows):
    df = pd.read_excel(excel_file,
                       sheet_name=sheet_name,
                       usecols=usecols,
                       header=header,
                       nrows=nrows)

    # Applying the styling to the DataFrame
    df = df.style.applymap(color_cells)
    return df

# Create expanders for tables
with st.expander("Table 1"):
    df1 = read_excel_and_style(sheet_name, 'E:H', 5, 6)
    st.dataframe(df1, hide_index=True)

with st.expander("Table 2"):
    df3 = read_excel_and_style(sheet_name, 'E:O', 29, 10)

    # Apply the formatting to the specific columns
    df3['Breadth'] = df3['Breadth'].apply(format_percentage_whole)
    df3['Closeness to 52 week'] = df3['Closeness to 52 week'].apply(format_percentage_one_decimal)
    df3['U/D'] = df3['U/D'].apply(format_percentage_one_decimal)
    
    # Apply styling and custom formatting to the DataFrame
    df3 = df3.style.applymap(yellow_background, subset=['median']).format({
        '3 month return': '{:.1f}',  # Format '3 month return' with 1 decimal place
        'median': custom_format  # Apply custom formatting to 'median' column
    })
    
    st.dataframe(df3, hide_index=True)





