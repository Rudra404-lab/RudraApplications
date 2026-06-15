import streamlit as st
st.markdown(":blue[Home Page.... Scroll Down to Login].")
st.image("image1.jpg")

st.header("Welcome! Please Login First")
t1=st.text_input("Username")
t2=st.text_input("Password",type="password")
b1=st.button("Sign In")

st.logo("logo1.png")


sidebar_css = """
<style>
[data-testid="stSidebar"] {
    background-color: #0068c9; /* Uses transparency */
}
</style>
"""
st.markdown(sidebar_css, unsafe_allow_html=True)
