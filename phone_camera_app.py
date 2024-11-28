'''
import streamlit as st
from streamlit_back_camera_input import back_camera_input

st.write("Camera test app")
from camera_input_live import camera_input_live

image = camera_input_live(debounce=10)

if image is not None:
    st.image(image)
else:
	st.write("none image")
'''

import cv2
import numpy as np
import streamlit as st

from camera_input_live import camera_input_live

"# Streamlit camera input live Demo"
"## Try holding a qr code in front of your webcam"

image = camera_input_live(debounce=100,show_controls=False)

if image is not None:
    st.image(image)
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    detector = cv2.QRCodeDetector()

    data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)

    if data:
        st.write("# Found QR code")
        st.write(data)
        with st.expander("Show details"):
            st.write("BBox:", bbox)
            st.write("Straight QR code:", straight_qrcode)