import streamlit as st
import re

# Function to check password strength
def check_strength(password):
    strength = 0

    # Length Check: +1 for each additional 4 characters
    if len(password) >= 8:
        strength += 1
    if len(password) >= 12:
        strength += 1
    if len(password) >= 16:
        strength += 1

    # Contains uppercase letter
    if re.search(r'[A-Z]', password):
        strength += 1
    
    # Contains lowercase letter
    if re.search(r'[a-z]', password):
        strength += 1
    
    # Contains digits
    if re.search(r'[0-9]', password):
        strength += 1
    
    # Contains special characters
    if re.search(r'[@#$%^&+=!]', password):  # Corrected this line
        strength += 1

    # Strength Meter Categories
    if strength <= 2:
        return "Weak", 25
    elif strength == 3:
        return "Moderate", 50
    elif strength == 4:
        return "Strong", 75
    elif strength >= 5:
        return "Very Strong", 100

# Streamlit UI
st.title("Password Strength Meter")

# User Input for password
password = st.text_input("Enter your password", type="password")

# Display password strength
if password:
    strength_label, strength_value = check_strength(password)
    st.write(f"Password Strength: {strength_label}")
    
    # Displaying the strength meter
    st.progress(strength_value)

    # Give suggestions
    if strength_value < 50:
        st.warning("Your password is weak. Consider using a mix of uppercase letters, lowercase letters, numbers, and special characters.")
    elif strength_value < 75:
        st.info("Your password is moderate. Adding more characters and special characters would improve the strength.")
    else:
        st.success("Your password is strong! Keep it up.")
