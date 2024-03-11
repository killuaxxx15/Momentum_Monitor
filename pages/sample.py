import pandas as pd
import streamlit as st
import random

# Create a sample DataFrame with multi-layer column headers
data = {
    ('Column AB', 'Column A'): [random.randint(1, 10) for _ in range(3)],
    ('Column AB', 'Column B'): [random.randint(1, 10) for _ in range(3)]
}

df = pd.DataFrame(data)

# Set the column index names
df.columns.names = ['Span', 'Column']

# Display the DataFrame in Streamlit
st.write("Table with Multi-Layer Column Headers")
st.dataframe(df, hide_index=True)
