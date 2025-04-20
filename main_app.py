import streamlit as st
from login import login  # Importing the login function
from heartPrediction_web_app1 import heart_prediction_page  # Importing the heart prediction function
from register import register

if 'valid_users' not in st.session_state:
    st.session_state.valid_users = {
        "admin": "password",
        "user1": "pass123",
        "user2": "mypassword"
    }
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    
def main():
    
    st.sidebar.title("Navigation")
    option = st.sidebar.selectbox("Choose an option", ["Register", "Login", "Heart Prediction"])
    
    if option == "Register":
        register()
    elif option == "Login":
          login()
    elif option == "Heart Prediction":
        if st.session_state.logged_in:
            heart_prediction_page()
        else:
            st.error("Please Login  to access the heart prediction page.")


    
   
# Entry point of the application
if __name__ == "__main__":
   main()
   