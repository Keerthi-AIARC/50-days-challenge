import streamlit as st

# App config
st.set_page_config(page_title="🔐 Password Checker", page_icon="🔑")

st.title("🔐 Password Strength Checker")
st.write("Check if your password meets the minimum security requirements.")

# Input field
password = st.text_input("Enter your password", type="password")

# Set your password rule
MIN_LENGTH = 8

# Check on button click
if st.button("Check Password"):
    if not password:
        st.warning("🚨 Please enter a password.")
    elif len(password) < MIN_LENGTH:
        st.error(f"❌ Password is too short. It must be at least {MIN_LENGTH} characters long.")
    else:
        st.success("✅ Good job! Your password meets the minimum length requirement.")

# Extra tip
st.info("Tip: For better security, use a mix of letters, numbers, and symbols. 🔒")

# Footer
st.caption("Built with ❤️ using Streamlit")
