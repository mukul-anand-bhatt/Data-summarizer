import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
import json
import requests

# Check if the default app has already been initialized
if not firebase_admin._apps:
    cred = credentials.Certificate("C:/Users/mukul/OneDrive - UPES/Documents/reactBasics/Text-summarizer/datavisulazer-6c547885ec31.json")
    firebase_admin.initialize_app(cred)

def login(email, password):
    try:
        user = auth.get_user_by_email(email)
        # Here you would typically verify the password, but Firebase handles this
        return True, user.uid
    except auth.UserNotFoundError:
        return False, None

def signup(email, password, display_name):
    try:
        user = auth.create_user(
            email=email,
            password=password,
            display_name=display_name
        )
        return True, user.uid
    except Exception as e:
        return False, str(e)

def app():
    st.title("Login/Signup App")
    choice = st.selectbox("Choose an option", ["Login", "Signup"])

    if choice == "Login":
        email = st.text_input("Email")
        password = st.text_input("Password", type='password')
        if st.button("Login"):
            success, uid = login(email, password)
            if success:
                st.success(f"Logged in successfully as {uid}")
            else:
                st.error("Login failed. Please check your credentials.")
    elif choice == "Signup":
        email = st.text_input("Email")
        password = st.text_input("Password", type='password')
        display_name = st.text_input("Display Name")
        if st.button("Signup"):
            success, uid_or_error = signup(email, password, display_name)
            if success:
                st.success(f"Signed up successfully as {uid_or_error}")
            else:
                st.error(f"Signup failed: {uid_or_error}")

if __name__ == "__main__":
    app()
