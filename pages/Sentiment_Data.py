import pandas as pd
import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title='Sentiment Data', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('Sentiment Data to be updated')

# Define Excel file and sheet name variables
excel_file = 'Sentimnet data.xlsx'
sheet_name = 'Sheet1'

# Cache data loading function for better performance
@st.cache
def load_excel_data(file_name, sheet, use_columns, header_row, num_rows):
    return pd.read_excel(file_name, sheet_name=sheet, usecols=use_columns, header=header_row, nrows=num_rows)

# TABLE 1
df1 = load_excel_data(excel_file, sheet_name, 'F:K', 10, 5)
df1 = df1.fillna('')
st.dataframe(df1, hide_index=True)
st.markdown(' ### ')

# TABLE 2
df2 = load_excel_data(excel_file, sheet_name, 'F:K', 19, 1)
df2 = df2.fillna('')
st.dataframe(df2, hide_index=True)
st.markdown(' ### ')


st.header('Bull/Bear Ratios')
st.image('pic1.png', caption='Figure 1', use_column_width=True)
st.image('pic2.png', caption='Figure 2', use_column_width=True)
st.image('pic3.png', caption='Figure 3', use_column_width=True)
st.image('pic4.png', caption='Figure 4', use_column_width=True)
st.image('pic5.png', caption='Figure 5', use_column_width=True)
st.image('pic6.png', caption='Figure 6', use_column_width=True)
st.image('pic7.png', caption='Figure 7', use_column_width=True)
st.image('pic8.png', caption='Figure 8', use_column_width=True)
st.image('pic9.png', caption='Figure 9', use_column_width=True)
st.image('pic10.png', caption='Figure 10', use_column_width=True)
st.image('pic11.png', caption='Figure 11', use_column_width=True)
st.image('pic12.png', caption='Figure 12', use_column_width=True)
st.image('pic13.png', caption='Figure 13', use_column_width=True)


