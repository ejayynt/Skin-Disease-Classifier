# Skin Disease Classifier

A deep learning–based skin disease classification system using convolutional neural networks (CNNs) and a Streamlit web application. This project demonstrates how computer vision and artificial intelligence can be applied in the healthcare domain for educational and research purposes.

## Overview
Early detection of skin diseases is crucial for effective treatment. This project uses a trained CNN model to classify skin disease images into multiple categories. Users can upload an image through a simple web interface and receive a predicted class along with a confidence score.

## Features
- Image-based skin disease classification
- CNN model built using TensorFlow/Keras
- Interactive Streamlit web interface
- Displays prediction confidence
- Supports multiple skin disease categories

## Supported Classes
- Actinic Keratoses (akiec)
- Basal Cell Carcinoma (bcc)
- Benign Keratosis-like Lesions (bkl)
- Dermatofibroma (df)
- Melanoma (mel)
- Melanocytic Nevi (nv)
- Vascular Lesions (vasc)

## Tech Stack
- Python
- TensorFlow / Keras
- NumPy
- Pillow (PIL)
- Streamlit

## Project Structure
```bash
skin-disease-classifier/
│
├── UI.py                    # Streamlit application
├── Skin detection.ipynb     # Model training and experiments
├── skin_disease_model.h5    # Trained CNN model
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

## How It Works
1. The user uploads a skin image through the Streamlit interface  
2. The image is resized and normalized  
3. The trained CNN model predicts the disease class  
4. The predicted class and confidence score are displayed to the user  

## Installation & Usage
1. Clone the repository
```bash
git clone https://github.com/your-username/skin-disease-classifier.git
cd skin-disease-classifier
```

## Dataset

This project is trained using a publicly available skin lesion dataset (such as HAM10000) for educational and research purposes only.

## Results

The model is capable of classifying common skin diseases with reasonable accuracy. Performance may vary depending on image quality, lighting conditions, and dataset distribution.

## Future Improvements

Improve accuracy using larger and more diverse datasets

Add explainability techniques such as Grad-CAM

Deploy the application online

Enhance UI and mobile compatibility
