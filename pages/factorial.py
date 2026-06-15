import streamlit as st
st.title("Factorial of a number")
num=st.number_input("enter a number:")
factorial=1
if num==0:
    factorial=1
else:
    for i in range(1,int (num+1)):
        factorial=factorial*i
st.success(f"The factorial of {num} is {factorial}")


st.code('''import streamlit as st
st.title("Factorial of a number")
num=st.number_input("enter a number:")
factorial=1
if num==0:
    factorial=1
else:
    for i in range(1,int (num+1)):
        factorial=factorial*i
st.success(f"The factorial of {num} is {factorial}")''')
