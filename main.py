import streamlit as st
import langchain_helper as hl

st.title("Restaurant name generator")

cuisine = st.sidebar.selectbox(
    "Choose a cuisine",
    ("Pakistan", "Singapore", "Bangladesh", "Taipei"),
)

if cuisine:
    response = hl.generate_restaurant_name_and_items(cuisine)


    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(",")
    st.write('Menu item')
    for menu_item in menu_items:
        st.write('-', menu_item)
