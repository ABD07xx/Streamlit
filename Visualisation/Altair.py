import streamlit as st 

import pandas as pd
import numpy as np
import altair as alt

#Scatter Plot
st.title("Altair Scatter Plot")
chart_data = pd.DataFrame(
    np.random.randn(500, 5),columns=['a', 'b', 'c','d','e'])

c = alt.Chart(chart_data).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c','d','e'])

st.altair_chart(c, use_container_width=True)


#Interactive Line Chart

df = pd.read_csv('lang_data.csv')


# Line Chart
lang_list = df.columns.tolist()
lang_choices = st.multiselect("Choose Language",lang_list,default='Bash')
new_df = df[lang_choices]
st.line_chart(new_df)

# Area Chart
st.area_chart(new_df,use_container_width=True)
