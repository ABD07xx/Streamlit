import streamlit as st

import pandas as pd
import numpy as np

st.title("Line Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3),
                          columns=['Line-1','Line-2','Line-3'])
st.line_chart(chart_data)

st.title("Area Chart")
st.area_chart(chart_data)


st.title("Bar Chart")
st.bar_chart(chart_data)

