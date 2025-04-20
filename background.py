# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 21:31:06 2024

@author: HP
"""

# background.py
import streamlit as st
import base64

def load_background():
    st.markdown(
    """
    Set a local image as the background using base64 encoding.
    :param image_path: Path to the local image file
    """
    <style>
        .stApp {
            background-image: url('https://i.ibb.co/0t3gDF5/IMG-20241215-WA0000-1734239323587.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

 load_background()
