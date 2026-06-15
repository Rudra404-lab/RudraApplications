import streamlit as st
st.title("Check whether Number is odd or even")
x=st.slider("select a number",1,500)
if x%2==0:
    st.success("Even Number")
else:
    st.success("Odd Number")


st.code('''import streamlit as st
st.title("Check whether Number is odd or even")
x=st.slider("select a number",1,500)
if x%2==0:
    st.success("Even Number")
else:
    st.success("Odd Number")
''')
