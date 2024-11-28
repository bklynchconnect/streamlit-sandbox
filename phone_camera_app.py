import streamlit as st
from streamlit_back_camera_input import back_camera_input

st.write("Camera test app")
pic = back_camera_input()
st.image(pic)