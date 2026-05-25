import streamlit as st 
import pandas as pd 
import plotly.express as px
 
# page - config 
st.set_page_config(page_title="SPD", layout="wide")
 
# title 
st.title("Student Performance Dashboard")
 
#data (creating samples) 
data = pd.DataFrame({
    "Name": ["Raja","Savitha", "Raji", "Ramar", "Bala"],
    "Math": [85, 90, 78, 88, 92], 
    "Science": [80, 85, 75, 90, 95], 
    "English": [78, 88, 70, 85, 90] 
})
 
# sidebar filter 
st.sidebar.header("Filter") 
student = st.sidebar.selectbox("select Student", data["Name"])
 
# filtered data 
filtered_data = data[data["Name"] == student]
 
# show the data 
st.subheader("Student Details")
st.dataframe(filtered_data)
 
# metrics 
st.subheader("Performance Summary") 
col1, col2, col3 = st.columns(3)
 
col1.metric("Math", int(filtered_data["Math"])) 
col2.metric("Science", int(filtered_data["Science"])) 
col3.metric("English", int(filtered_data["English"]))
 
# chart data 
chart_data = filtered_data.melt(id_vars=["Name"],
                                var_name="Subject", 
                                value_name="Marks"
                               )
#bar chart 
st.subheader("Bar Chart - Mark comparison") 
fig = px.bar(chart_data, x="Subject", y ="Marks",  color ="Subject") 
st.plotly_chart(fig, use_container_width = True)
 
# line chart 
st.subheader("Line Chart - Class comparison")  
st.line_chart(data.set_index("Name"))