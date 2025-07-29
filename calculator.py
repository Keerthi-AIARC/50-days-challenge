import streamlit as st

# Title
st.title("🧮 Simple Calculator")

# Input fields
num1 = st.number_input("Enter first number", format="%.2f")
num2 = st.number_input("Enter second number", format="%.2f")

# Operation selection
operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate result on button click
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"The result is: {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"The result is: {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"The result is: {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result is: {result}")
        else:
            st.error("Cannot divide by zero!")

# Footer
st.caption("✅ Developed by Keerthi - Twin-D DigiGrowth")
