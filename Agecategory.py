import streamlit as st

# Page configuration
st.set_page_config(page_title="Age Group Classifier", page_icon="🎂")

# Title
st.title("🎂 Age Group Classifier")

# Input
age = st.number_input("Enter your age:", min_value=0, step=1)

# Check Button
if st.button("Check Age Group"):
    if age <= 12:
        st.success("🧒 You are a **Child**.")
    elif 13 <= age <= 19:
        st.info("👱 You are a **Teenager**.")
    elif 20 <= age <= 59:
        st.warning("🧑 You are an **Adult**.")
    else:
        st.error("👴 You are a **Senior**.")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
