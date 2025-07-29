import streamlit as st

# Page configuration
st.set_page_config(page_title="🧾 Item Cost Calculator", page_icon="💰")

st.title("🛒 Total Cost Calculator (with Tax)")

st.write("Enter the prices of your items and tax percentage to calculate the total amount.")

# Number of items
num_items = st.slider("How many items do you want to enter?", 3, 5)

# Input item prices
item_prices = []
for i in range(num_items):
    price = st.number_input(f"Enter price for Item {i+1} (₹)", min_value=0.0, step=1.0, format="%.2f")
    item_prices.append(price)

# Tax input
tax_percent = st.number_input("Enter tax percentage (%)", min_value=0.0, step=0.1, format="%.2f")

# Calculate button
if st.button("Calculate Total"):
    subtotal = sum(item_prices)
    tax_amount = (subtotal * tax_percent) / 100
    total = subtotal + tax_amount

    st.markdown(f"### 🧾 Summary")
    st.write(f"Subtotal: ₹{subtotal:.2f}")
    st.write(f"Tax Amount ({tax_percent}%): ₹{tax_amount:.2f}")
    st.success(f"**Total Amount (with Tax): ₹{total:.2f}**")

# Footer
st.markdown("---")
st.caption("🧮 Built using Streamlit")
