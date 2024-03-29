import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
import json
import requests
import base64

# Check if the default app has already been initialized
if not firebase_admin._apps:
    cred = credentials.Certificate("C:/Users/mukul/OneDrive - UPES/Documents/reactBasics/Text-summarizer/datavisulazer-6c547885ec31.json")
    firebase_admin.initialize_app(cred)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover; opacity: 1.2; 
        filter: brightness(1.5); top: 8;
        left: 5;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def login(email, password):
    try:
        user = auth.get_user_by_email(email)
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
    # Set the background image
    set_background('C:/Users/mukul/OneDrive - UPES/Documents/reactBasics/Text-summarizer/3486_img8080696789868880.jpg')
    
    # Custom CSS for selectbox
    st.markdown("""
    <style>
    .title {
        color: #1234FF; /* Change text color */
        background-color: #FFFFFF; /* Change background color */
        opacity: 1; /* Adjust opacity for transparency */
        filter: brightness(1.5); /* Increase brightness */
    }
    </style>
    """, unsafe_allow_html=True)
    
    
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
