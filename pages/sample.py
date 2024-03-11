import pandas as pd
import streamlit as st
import random

# Create a sample DataFrame with multi-layer column headers
data = [
    [random.randint(1, 10) for _ in range(2)]
    for _ in range(3)
]

columns = pd.MultiIndex.from_tuples(
    [('Column AB', 'Column A'), ('Column AB', 'Column B')]
)

df = pd.DataFrame(data, columns=columns)

# Display the DataFrame in Streamlit
st.write("Table with Multi-Layer Column Headers")
st.dataframe(df, hide_index=True)
