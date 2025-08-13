import streamlit as st
import string
import secrets
import re

# Your original generate_password function stays exactly as it is
def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    if nums + special_chars + uppercase + lowercase > length:
        raise ValueError("Sum of character constraints exceeds password length.")
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_characters = letters + digits + symbols
    while True:
        password = ''
        for _ in range(length):
            password += secrets.choice(all_characters)
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]
        if all(constraint <= len(re.findall(pattern, password))
               for constraint, pattern in constraints):
            break
    return password

# Streamlit UI
st.title("Password Generator")

length = st.number_input("Password length", min_value=1, value=16)
nums = st.number_input("Number of digits", min_value=0, value=1)
special_chars = st.number_input("Number of special characters", min_value=0, value=1)
uppercase = st.number_input("Number of uppercase letters", min_value=0, value=1)
lowercase = st.number_input("Number of lowercase letters", min_value=0, value=1)

if st.button("Generate Password"):
    try:
        password = generate_password(length, nums, special_chars, uppercase, lowercase)
        st.write("Generated Password:", password)
    except ValueError as e:
        st.error(e)
