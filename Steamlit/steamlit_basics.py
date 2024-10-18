import streamlit as st

st.title('Hello, Devlopers')
st.header('Welcome to Streamlit Basics')
st.subheader('This is a subheader')
st.write('## This is a paragraph of text')
st.code('print("Hello, World!")')
Name=st.text_input('Enter Your Name :')
Date=st.date_input('Selectde  Date :')


if st.button('Click Me!'):
    st.write('Welcome, ' + Name + '!')
    st.write('Selected Date :',Date)
