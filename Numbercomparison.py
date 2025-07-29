import streamlit as st

# Page settings
st.set_page_config(page_title="🔢 Number Comparator", page_icon="🔍")

st.title("🔍 Compare Two Numbers")

st.write("Enter two numbers to find which one is larger, smaller, or if they are equal.")

# Input numbers
num1 = st.number_input("Enter First Number", step=1.0)
num2 = st.number_input("Enter Second Number", step=1.0)

# Compare on button click
if st.button("Compare"):
    if num1 > num2:
        st.success(f"{num1} is **larger** than {num2}")
        st.info(f"{num2} is **smaller** than {num1}")
    elif num1 < num2:
        st.success(f"{num2} is **larger** than {num1}")
        st.info(f"{num1} is **smaller** than {num2}")
    else:
        st.warning("Both numbers are **equal**!")

# Footer
st.markdown("---")
st.caption("📊 Built using Streamlit")
