import pandas as pd
import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title='Cash Model', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('Cash Model')

# Display the last update date
st.markdown('#### Updated: 14/06/2024')

# Define Excel file and sheet name variables
excel_file = 'Cash_model_14_06_2024.xlsx'
sheet_name = 'Sheet1'


# Cache data loading function for better performance
@st.cache_data
def load_excel_data(file_name, sheet, use_columns, header_row, num_rows):
    return pd.read_excel(file_name, sheet_name=sheet, usecols=use_columns, header=header_row, nrows=num_rows)

# Define a function to format numbers
def format_number(val):
    if pd.isna(val) or val == '':
        return ''
    try:
        val = float(val)
        if val.is_integer():
            return "{:.0f}".format(val)
        else:
            return "{:.2f}".format(val)
    except ValueError:
        return val


# TABLE 1
df1 = load_excel_data(excel_file, sheet_name, 'C:H', 7, 9)
df1 = df1.fillna('')
df1 = df1.applymap(format_number)
st.markdown('### Table 1')
st.dataframe(df1, hide_index=True)

# TABLE 2
df2 = load_excel_data(excel_file, sheet_name, 'C:E', 19, 1)
st.markdown('### Table 2')
st.dataframe(df2, hide_index=True)
