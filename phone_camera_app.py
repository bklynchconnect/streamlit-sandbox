import streamlit as st
from streamlit_back_camera_input import back_camera_input

st.write("Camera test app")
from camera_input_live import camera_input_live

image = camera_input_live(debounce=100)

if image is not None:
    st.image(image)