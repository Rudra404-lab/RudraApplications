import streamlit as st
st.title("Greater number B/w two numbers")
t1=st.number_input("Enter 1st number")
t2=st.number_input("Enter 2st number")
b1=st.button("Find Greater")
if (t1>t2):
    st.success(f"Greater number={t1}")
else:
    st.success(f"Greater number={t2}")

st.code('''import streamlit as st
st.title("Greater number B/w two numbers")
t1=st.number_input("Enter 1st number")
t2=st.number_input("Enter 2st number")
b1=st.button("Find Greater")
if (t1>t2):
    st.success(f"Greater number={t1}")
else:
    st.success(f"Greater number={t2}")''')
