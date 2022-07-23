import streamlit as st
from PIL import Image

@st.cache
def view_image(image_file):
    img = Image.open(image_file)
    return img