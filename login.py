# login.py
import streamlit as st

# login.py

def login():
    st.title("Welcome")
    st.markdown(
       """
       <style>
       .stApp {
           background-image: url('https://www.merillife.com/assets/images/blog/wQe218SrHyI7X0zPfDpW.jpg');
           background-size: cover;
           background-position: center;
           background-repeat: no-repeat;
           height: 100vh;
       }
       </style>
       """,
       unsafe_allow_html=True)
    st.title("Login Page")
    
    username = st.text_input("**Username**").strip()
    password = st.text_input("*******Password*******", type='password').strip()
    
    if st.button("Login"):
        if username in st.session_state.valid_users and st.session_state.valid_users[username] == password:
            st.success("Login successful!")
            st.session_state.logged_in = True  # Set logged_in to True
        else:
            st.error("Invalid username or password.")
