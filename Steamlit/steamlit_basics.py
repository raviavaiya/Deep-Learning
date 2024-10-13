import streamlit as st

st.title('Hello, Devlopers')
st.header('Welcome to Streamlit Basics')
st.subheader('This is a subheader')
st.write('This is a paragraph of text')
st.code('print("Hello, World!")')
Name=st.text_input('Enter Your Name :')

if st.button('Click Me!'):
    st.write('Welcome, ' + Name + '!')