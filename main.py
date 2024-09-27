import streamlit as st
from langchain_helper import generate_restaurant_name_and_items

st.title("Site Name")

cuisine=st.sidebar.selectbox("Pick a cuisine",("Indian","Italian","Mexico","Arabic","American"))

if cuisine:
    response=generate_restaurant_name_and_items(cuisine)
    st.header(response["restaurant_name"].strip())
    menu_items=response['menu_items'].strip().split(",")
    st.write("** Menu Item **")
    for item in menu_items:
        st.write("-",item)



