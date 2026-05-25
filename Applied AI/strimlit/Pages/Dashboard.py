import streamlit as st 

import pandas as pd
 
 
st.title("Dashboard")
 
data = pd.DataFrame({

    "Day": ["Mon", "Tue", "Wed"], 

    "Sales": [120,98,143]

})
 
st.write(data) 

st.line_chart(data.set_index("Day"))