import streamlit as st

# Page title
st.set_page_config(page_title="Even or Odd Checker", page_icon="🔢")
st.title("🔍 Even or Odd Number Checker")

st.header("1️⃣ Single Number Checker")
number = st.number_input("Enter a number:", step=1)

if st.button("Check"):
    if number % 2 == 0:
        st.success(f"✅ The number {int(number)} is **Even**.")
    else:
        st.warning(f"🔹 The number {int(number)} is **Odd**.")

st.markdown("---")

st.header("2️⃣ List of Numbers Checker")
num_list_input = st.text_input("Enter numbers separated by commas (e.g., 1, 2, 3, 4):")

if st.button("Check List"):
    if num_list_input:
        try:
            # Convert input string to list of integers
            num_list = [int(x.strip()) for x in num_list_input.split(",")]

            results = []
            for num in num_list:
                status = "Even ✅" if num % 2 == 0 else "Odd 🔹"
                results.append(f"{num} ➤ {status}")

            st.subheader("Results:")
            st.write("\n".join(results))
        except ValueError:
            st.error("❌ Please enter only valid integers separated by commas.")
    else:
        st.warning("⚠️ Please enter a list of numbers first.")
