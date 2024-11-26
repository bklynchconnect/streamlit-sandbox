import streamlit as st

pic = st.camera_input("Camera")

if pic:
    st.image(pic)