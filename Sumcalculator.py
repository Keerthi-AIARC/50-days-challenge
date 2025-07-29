import streamlit as st

st.set_page_config(page_title="Sum 1 to N", page_icon="➕")

st.title("➕ Sum of Numbers from 1 to N")

# Input for the number
n = st.number_input("Enter a positive integer (N):", min_value=1, step=1)

# Button to calculate sum
if st.button("Calculate Sum"):
    total = 0
    for i in range(1, int(n) + 1):
        total += i

    st.success(f"The sum of numbers from 1 to {int(n)} is: {total}")
