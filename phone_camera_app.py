import streamlit as st
from streamlit_back_camera_input import back_camera_input

st.write("Camera test app")
from camera_input_live import camera_input_live

"# Streamlit camera input live Demo"
"## Try holding a qr code in front of your webcam"

image = camera_input_live()

if image is not None:
    st.image(image)