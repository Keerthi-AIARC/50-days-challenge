import streamlit as st

st.set_page_config(page_title="Number Counter", page_icon="🔢")

st.title("🔢 Count Positive, Negative, and Zero Numbers")
st.write("Enter a list of numbers separated by commas (e.g., `5, -2, 0, 7, -1`)")

# Input
number_input = st.text_input("Your numbers:")

if st.button("Count"):
    try:
        # Convert string to list of integers
        number_list = [int(x.strip()) for x in number_input.split(',')]
        
        positives = sum(1 for num in number_list if num > 0)
        negatives = sum(1 for num in number_list if num < 0)
        zeros = sum(1 for num in number_list if num == 0)
        
        st.success(f"✅ Results:")
        st.write(f"🔹 Positive Numbers: {positives}")
        st.write(f"🔹 Negative Numbers: {negatives}")
        st.write(f"🔹 Zeros: {zeros}")
    except ValueError:
        st.error("Please enter only numbers separated by commas.")
