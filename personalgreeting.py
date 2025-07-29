import streamlit as st

# Friendly color name mapper
COLOR_NAMES = {
    "#FF0000": "Red",
    "#0000FF": "Blue",
    "#008000": "Green",
    "#FFFF00": "Yellow",
    "#FFA500": "Orange",
    "#800080": "Purple",
    "#FFC0CB": "Pink",
    "#A52A2A": "Brown",
    "#000000": "Black",
    "#FFFFFF": "White",
    "#808080": "Gray"
}

def get_friendly_color_name(hex_color):
    # Convert to uppercase to match keys
    hex_color = hex_color.upper()
    # Return friendly name or the hex code as fallback
    return COLOR_NAMES.get(hex_color, f"that lovely shade ({hex_color})")

# Page settings
st.set_page_config(page_title="🎨 Personalized Greeting App")

# Title
st.title("🌟 Hey There! Let's Make a Fun Greeting!")

# User Inputs
name = st.text_input("👤 What's your name?")
age = st.number_input("🎂 How old are you?", min_value=1, max_value=120, step=1)
color = st.color_picker("🌈 Pick your favorite color:")

# Generate Greeting
if st.button("✨ Generate Greeting"):
    if name and age:
        friendly_color = get_friendly_color_name(color)
        st.markdown(f"""
        <div style='
            background-color:#f0f0f0;
            border: 2px dashed {color};
            padding: 20px;
            border-radius: 15px;
        '>
            <h2 style='color:{color}'>🎈 Hello, {name}!</h2>
            <p style='font-size:18px'>
                You're {age} years young and full of energy! 🎉<br>
                We love your taste — {friendly_color} is such a great choice! 🖌️<br><br>
                Keep smiling and painting the world in your own colors! 💫
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("🚨 Please fill in both your name and age to receive your greeting.")


