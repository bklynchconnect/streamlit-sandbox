import streamlit as st

st.write("Camera test app")
pic = st.camera_input("Camera")

if pic:
    st.image(pic)