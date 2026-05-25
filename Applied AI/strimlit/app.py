# import streamlit as st
 
# #title 

# st.title("My First Streamlit App")
 
# #Text

# st.write("Welcome You!!!")
 
# #input 

# name = st.text_input("Enter your Name:")
 
# #button-action 

# if st.button("Submit"):

#     st.success(f"Hello, {name}!")


# Main File Python - app.py file
 
# 1. Sidebar navigation 
# 2. Text input & sliders
# 3. Data & tables 
# 4. Image & Video 
# 5. Form handling 
# 6. layout  
 
import streamlit as st 
import pandas as pd
 
# page config. 
st.set_page_config(
    page_title = "UI Demo App", 
    page_icon = "icon.png",
    layout = "wide" 
)
 
# title 
st.title("Streamlit User Interface App")
 
# sidebar 
st.sidebar.header("Navigation") 
option = st.sidebar.radio("Go to :", ["Home", "Data", "Media", "Form", "Counter"])
 
# Home  
if option == "Home": 
    st.header("Home") 
    st.write("Welcome to Streamlit UI Home Page")  
 
    name = st.text_input("Enter your name") 
    age = st.slider("Select Your Age:", 1,100)
 
    if st.button("Greet"):
        st.success(f"Hello {name}, you are {age} old.!!")
 