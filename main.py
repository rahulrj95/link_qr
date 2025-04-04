import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

st.title("QR Code Generator")

# Input for QR Code
text = st.text_input("Enter text or URL:")

if text:
    qr = qrcode.make(text)  # Generates a QR code as a PIL Image

    # Convert PIL image to bytes
    img_bytes = BytesIO()
    qr.save(img_bytes, format="PNG")
    img_bytes = img_bytes.getvalue()  # Get byte data

    # Display the QR Code
    st.image(img_bytes, caption="Generated QR Code")