import numpy as np
import pandas as pd
import requests
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_lottie import st_lottie
import json
import os
from streamlit_option_menu import option_menu
from streamlit_timeline import timeline

st.set_page_config(page_title="Welcome", page_icon="👋", layout="wide", initial_sidebar_state="collapsed", menu_items={'Get Help': 'https://www.extremelycoolapp.com/help','Report a bug': "https://www.extremelycoolapp.com/bug",'About': "# This is a header. This is an *extremely* cool app!"})

# def load_animation(name_ending: str):
#     # Assume all JSON files start with "animation_" and end with the specified ending
#     json_filename = f"animation_{name_ending}.json"
#     json_path = os.path.join("src", "media", json_filename)
    
#     try:
#         with open(json_path, "r") as file:
#             lottie_animation = json.load(file)
#         st_lottie(lottie_animation, speed=2, height=200, key="initial")
#     except:
#         st.warning(f"Failed to load Lottie animation for {json_filename}.")

# load_animation("girl_with_laptop")

st.title('Hey, I\'m Karyna.')
st.subheader('I\'ve developed analytics tools for traders in the biggest hedge fund in the world - Bridgewater, and am currently building a machine learning algorithm at Goodyear.')

# EXPERIMENTAL CV

with open("src/Karyna_Zuyeva.pdf", "rb") as file:
    btn=st.download_button(
    label="Download CV",
    data=file,
    file_name="Karyna_Zuyeva_CV.pdf",
    mime="application/octet-stream"
)

