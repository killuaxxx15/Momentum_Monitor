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
    df2 = read_excel_and_style(sheet_name, 'E:J', 13, 14)
    
    # List of columns to be converted to integers
    columns_to_int = ['3 month return', '6 month rank']
    
    # Iterate through columns and fill NaN with empty string for non-numeric columns
    for col in df2.columns:
        if col not in columns_to_int:
            df2[col] = df2[col].fillna('')

    # Convert '3 month return' and '6 month rank' to integers
    # First replace NaN with 0 or any other default integer value
    df2['3 month return'] = df2['3 month return'].fillna(0).round().astype(int)
    df2['6 month rank'] = df2['6 month rank'].fillna(0).round().astype(int)

    st.dataframe(df2, hide_index=True)





