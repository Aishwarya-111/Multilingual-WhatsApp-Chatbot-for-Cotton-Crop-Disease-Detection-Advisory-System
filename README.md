# Multilingual-WhatsApp-Chatbot-for-Cotton-Crop-Disease-Detection-Advisory-System
# 🌿 Multilingual WhatsApp Chatbot for Cotton Crop Disease Detection & Advisory System

## Overview

This project is a multilingual WhatsApp chatbot developed to assist cotton farmers in identifying crop diseases and obtaining advisory information in their preferred language.
Farmers can upload a cotton leaf image through WhatsApp, and the system predicts the disease using a trained deep learning model. Based on the predicted disease, the chatbot provides advisory recommendations and management suggestions.
The chatbot supports English, Hindi, and Telugu, making it more accessible to farmers from different regions.
In addition to image-based disease detection, the system also supports predefined text and voice queries related to cotton crop advisory.
The chatbot combines Deep Learning, Computer Vision, Natural Language Processing, Speech Processing, and Explainable AI to create an accessible digital assistant for farmers.

## Features

* Cotton leaf disease detection from uploaded images
* Multilingual support (English, Hindi, Telugu)
* WhatsApp-based interaction using Twilio
* Rule-based agricultural advisory recommendations
* Support for predefined text queries
* Support for predefined voice queries
* Explainable AI using Grad-CAM visualizations
* Automated disease-specific recommendations

## Dataset

The disease classification model was trained using the SAR-CLD-2024 cotton leaf disease dataset available on Mendeley Data.

Dataset Source:
https://data.mendeley.com/datasets/b3jy2p6k8w/2

**🔍 Cotton Disease Detection**

Detects the following cotton leaf conditions:

Bacterial Blight

Curl Virus

Healthy Leaf

Herbicide Growth Damage

Leaf Hopper/Jassids

Leaf Reddening

Leaf Variegation


**🌐 Multilingual Support**

Supported Languages:

English

Hindi

Telugu

**🛠️ Technology Stack**

**Programming Language:**

Python


**Frameworks & Libraries:**

Flask

TensorFlow / Keras

OpenCV

NumPy

Matplotlib

Pillow


APIs & Services:

Twilio WhatsApp API

Google Translate

SpeechRecognition

gTTS


**Explainable AI:**

Grad-CAM

## How It Works

1. The farmer sends a cotton leaf image through WhatsApp.
2. The image is processed by the trained deep learning model.
3. The system predicts the most likely disease.
4. Disease-specific advisory information is retrieved.
5. The chatbot responds with:
   * Predicted disease
   * Confidence score
   * Advisory recommendations
6. A Grad-CAM visualization is generated to highlight the image regions used for prediction.

The chatbot also handles a set of predefined agricultural text and voice queries and responds with corresponding advisory information.

## Technologies Used

* Python
* TensorFlow / Keras
* Flask
* OpenCV
* NumPy
* Matplotlib
* Twilio WhatsApp API
* SpeechRecognition
* Google Translate
* gTTS
* Grad-CAM

## Installation

### Clone the Repository

```bash
git clone https://github.com/Aishwarya-111/Multilingual-WhatsApp-Chatbot-for-Cotton-Crop-Disease-Detection-Advisory-System.git
```

### Navigate to the Project Folder

```bash
cd Multilingual-WhatsApp-Chatbot-for-Cotton-Crop-Disease-Detection-Advisory-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a file named `.env` in the project root directory:

```env
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
```

### Run the Application

```bash
python app.py
```
The Flask server will start locally and wait for incoming WhatsApp webhook requests.

## WhatsApp Integration

To connect the chatbot with WhatsApp:

1. Create a Twilio account.
2. Enable the Twilio WhatsApp Sandbox.
3. Start the Flask application.
4. Expose the local server using ngrok:

```bash
ngrok http 5000
```
5. Copy the generated HTTPS URL.
6. Configure the Twilio webhook URL:

```text
https://your-ngrok-url/api/v1/webhook
```
7. Send messages to the Twilio Sandbox WhatsApp number.

## Explainable AI

The project uses Grad-CAM (Gradient-weighted Class Activation Mapping) to visualize the regions of the cotton leaf image that contribute most to the model's prediction. This helps in understanding and interpreting the model's decision-making process.

## Author
Ch. Aishwarya Sulochana 

B.Tech in Electronics and Instrumentation Engineering

Minor in Data Science

VNR Vignana Jyothi Institute of Engineering & Technology
