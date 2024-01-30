import urllib.request
import numpy as np
import pandas as pd
import requests
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_lottie import st_lottie
import json
import os
from streamlit_option_menu import option_menu

import streamlit as st
from streamlit_option_menu import option_menu

def load_animation(name_ending: str):
    # Assume all JSON files start with "animation_" and end with the specified ending
    json_filename = f"animation_{name_ending}.json"
    json_path = os.path.join("src", "media", json_filename)
    
    try:
        with open(json_path, "r") as file:
            lottie_animation = json.load(file)
        st_lottie(lottie_animation, speed=2, height=200, key="initial")
    except:
        st.warning(f"Failed to load Lottie animation for {json_filename}.")

load_animation("girl_with_laptop")

st.header('Hey, I\'m Karyna - A Data Scientist from Ukraine.', divider='rainbow')
st.text('I\'ve developed analytics tools for traders in the biggest hedge fund in the world - Bridgewater, and am currently building a machine learning algorithm at Goodyear.')


# EXPERIMENTAL CV

with open("src/Karyna_Zuyeva.pdf", "rb") as file:
    btn=st.download_button(
    label="Download CV",
    data=file,
    file_name="Karyna_Zuyeva_CV.pdf",
    mime="application/octet-stream"
)

