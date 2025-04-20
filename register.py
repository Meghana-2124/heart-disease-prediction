# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 18:32:46 2024

@author: HP
"""
import streamlit as st


def register():
    st.title("Register New User")
    st.markdown(
       """
       <style>
       .stApp {
           background-image: url('https://www.shutterstock.com/image-vector/abstract-red-human-heart-transparent-600nw-2324709287.jpg');
           background-size: cover;
           background-position: center;
           background-repeat: no-repeat;
           height: 100vh;
       
       }
       </style>
       """,
       unsafe_allow_html=True)
    
    new_username = st.text_input("****New Username****").strip()
    new_password = st.text_input("**New Password**", type='password').strip()
    
    if st.button("**Register**"):
        if new_username in st.session_state.valid_users:
            st.error("Username already exists. Please choose a different username.")
        elif new_username == "":
            st.error("Username cannot be empty.")
        elif new_password == "":
            st.error("Password cannot be empty.")
        else:
            # Add the new user to the valid_users
            st.session_state.valid_users[new_username] = new_password
            st.success("**Registration successful! You can now log in.**")
