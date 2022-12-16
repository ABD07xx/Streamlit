import streamlit as st 
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport




df = pd.read_csv("tips.csv")




profile = ProfileReport(df,

        title="Tips Data",

    variables={

        "descriptions": {

            "total_bill": "Total Bill",

            "tip": "Tip",

            "sex": "Sex",

            "smoker": "Smoke",

            "day": "Day",

            "time": "Time",

            "size": "Chairs Occupied",




        }

    }

)


st.title("Pandas Profiling for Tips in Streamlit!")

st.write(df)

st_profile_report(profile)