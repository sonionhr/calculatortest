import streamlit as st

st.title("My Calculator App")
number1 = st.number_input("Insert first number")
number2 = st.number_input("Insert second number")

if st.button('Calculate'):
    st.write('The result is ', number1 + number2)
