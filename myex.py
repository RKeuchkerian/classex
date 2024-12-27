import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dashboard title
st.title("Interactive Dashboard")

# Subtitle
st.subheader("Example with charts, tables and controls")

# Loading data
df = pd.read_cv('dfdropna')

# Bar chart
st.bar_chart(df.set_index('Category'))

# Display table
st.write("Data Table:")
st.dataframe(df)

# Slider control
value = st.slider("Select a value", 0, 300, 150)

# Filter data based on slider
df_filtrado = df[df['Values'] <= value]

# Show filtered data
st.write(f"Filtered data with values ​​<= {value}:")
st.dataframe(df_filtrado)