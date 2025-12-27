import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Load model and label map
model = load_model("skin_disease_model.h5")
class_names = [
    "akiec",
    "bcc",
    "bkl",
    "df",
    "mel",
    "nv",
    "vasc",
]

st.title("🧴 Skin Disease Classifier")
st.write(
    "Upload a skin image and get a prediction. This is for educational purposes only."
)

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).resize((64, 64))
    st.image(image, caption="Uploaded Image", use_container_width=True)

    img_array = np.array(image) / 255.0
    prediction = model.predict(img_array.reshape(1, 64, 64, 3))
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    st.subheader(f"Prediction: {predicted_class}")
    st.write(f"Confidence: {confidence:.2f}%")
    st.markdown(
        "⚠️ This prediction is not a medical diagnosis. Please consult a professional."
    )
