import streamlit as st
st.title("Check whether a number is prime or not")
n=st.slider("Pick a number",1,100)
f=0
for i in range(1,n+1):
    if n%i==0:
        f=f+1
if f==2:
    st.success("PRIME NUMBER")
else:
    st.success("NOT A PRIME NUMBER")

st.code('''import streamlit as st
st.title("Check whether a number is prime or not")
n=st.slider("Pick a number",1,100)
f=0
for i in range(1,n+1):
    if n%i==0:
        f=f+1
if f==2:
    st.success("PRIME NUMBER")
else:
    st.success("NOT A PRIME NUMBER")''')
