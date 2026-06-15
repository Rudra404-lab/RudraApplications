import streamlit as st
st.title("S i g n U p")
t1=st.text_input("Username")
t2=st.text_input("Password",type="password")
t3=st.text_input("Mobile Number")
t4=st.text_input("Email Id")
t5=st.date_input("DOB")


b1=st.button("SIGN UP")
