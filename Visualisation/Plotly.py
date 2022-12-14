# Core Pkgs
import streamlit as st 

# Load EDA Pkg
import pandas as pd 
import numpy as np 

# Load Data Vis Pkg
import plotly.express as px
import plotly.figure_factory as ff

st.title("Visualisations using Plotly")
df = pd.read_csv('tips.csv')
st.dataframe(df.head(5))


st.write("Pie Chart type 1")
fig = px.pie(df, values="total_bill", names="day")
st.plotly_chart(fig)


st.write("Pie Chart type 2")
fig = px.pie(df, values="total_bill", names="day",
             color_discrete_sequence=px.colors.sequential.RdBu,
             opacity=0.7, hole=0.5)
st.plotly_chart(fig)



st.write("Interactive Visualisation using plotly")

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)