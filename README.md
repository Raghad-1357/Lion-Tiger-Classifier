# 🦁🐯 Image Classification with Teachable Machine

This project uses a **pre-trained image classification model** created using [Teachable Machine](https://teachablemachine.withgoogle.com/) to distinguish between two animal classes: **Lion** and **Tiger**.

## ✅ Project Overview
- Tool used: [Teachable Machine by Google](https://teachablemachine.withgoogle.com/)
- Model type: Image classification (Standard Image Model)
- Classes:
  - `Lion`
  - `Tiger`
- Framework used: TensorFlow + Keras
- Execution environment: [Google Colab](https://colab.research.google.com/)

## 📁 Files in the Project
| File Name          | Description                                  |
|--------------------|----------------------------------------------|
| `keras_model.h5`   | The trained Keras model                     |
| `labels.txt`       | Text file containing class labels           |
| `test_image.jpg`   | Sample image used to test the model         |
| `predict.py`       | Python script to load model and make prediction |
| `screenshot.png`   | Screenshot showing prediction output        |

## 🚀 How to Run the Project in Google Colab
1. Upload the following files to your Colab session:
   - `keras_model.h5`
   - `labels.txt`
   - `test_image.jpg`
   - `predict.py` *(you can also paste the code directly in a cell)*

2. Run the script:
You should see output like:
Class: Lion
Confidence Score: 0.98

📸 Screenshot  
*i will put pic here 😁*

## 🎓 Credits
Created as part of a machine learning assignment using Google Teachable Machine and Colab.
