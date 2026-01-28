🖋 Intelligent Signature Forgery Detection System

An AI-powered web application that detects and compares handwritten signatures to identify genuine and forged signatures using Deep Learning (CNN) and Computer Vision.

📌 Problem Statement (Short)

Handwritten signatures are widely used for authentication in banking, legal, and administrative processes. Manual verification of signatures is time-consuming, subjective, and prone to human error, especially with large volumes of documents. This project aims to develop an intelligent, automated signature forgery detection system that accurately distinguishes between genuine and forged signatures using deep learning techniques, thereby improving security, efficiency, and reliability.

💡 Solution Overview

This system uses a Convolutional Neural Network (CNN) trained on grayscale signature images to learn distinguishing features such as stroke patterns, curvature, and texture.
Users can upload two signature images through a web interface, and the system analyzes both signatures to determine which one is real and which one is forged, based on model confidence scores.

🗂 Project Structure
```text
signature_project/
│
├── app.py                         # Flask backend
├── signature_model_safe/          # Trained CNN model (SavedModel format)
│
├── dataset/                       # Training & testing dataset
│   ├── train/
│   └── test/
│
├── static/
│   ├── style.css                  # UI styling
│   └── script.js                  # Frontend logic (AJAX, UI updates)
│
├── templates/
│   └── index.html                 # Main frontend page
│
├── train_cnn.py                   # Model training script
├── predict_single.py              # Single image prediction script
└── README.md
```

🛠 Tech Stack
🔹 Machine Learning

- TensorFlow 2.13.1
- Keras (via TensorFlow)
- OpenCV
- NumPy

🔹 Backend

- Flask (Python)

🔹 Frontend

- HTML5
- CSS3
- JavaScript (Vanilla)

🔹 Tools

- Python 3.10
- Virtual Environment (venv)

⚙️ How It Works

1. User uploads two signature images

2. Images are preprocessed (grayscale, resized, normalized)

3. CNN model predicts confidence scores for both signatures

4. The system compares confidence scores

5. Signature with higher confidence is labeled REAL, the other FORGED

🚀 How to Run the Project Locally
✅ Prerequisites

- Python 3.10 (recommended)
- pip
- Git

🔹 Step 1: Clone the Repository
```
git clone https://github.com/your-username/intelligent-signature-forgery-detection.git
cd intelligent-signature-forgery-detection
```

🔹 Step 2: Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate   # Windows
```

🔹 Step 3: Install Dependencies
```
pip install --upgrade pip
pip install flask tensorflow==2.13.1 opencv-python numpy matplotlib
```

🔹 Step 4: Run the Flask App
```
python app.py
```

🔹 Step 5: Open in Browser
http://127.0.0.1:5000

📊 Model Details

- Input size: 128 × 128 grayscale images

- Architecture: Convolutional Neural Network (CNN)

- Output: Binary classification (Real / Forged)

- Activation: Sigmoid

- Loss function: Binary Crossentropy

- Optimizer: Adam

🎯 Key Features

- Upload and compare two signatures

- AI-based real vs forged decision

- Clean and interactive web UI

- End-to-end ML pipeline

- Scalable and extensible design

🔮 Future Enhancements

- Support for bulk signature verification

- Signature authenticity explanation heatmaps

- User authentication and history tracking

- Deployment on cloud platforms

- Improved accuracy with data augmentation

👨‍💻 Author

Meet Parmar | B.Tech | Computer Engineering | Gcet

Kathan Majithia | B.Tech | Computer Engineering | Gcet

Meera Sharma | B.Tech | Computer Engineering | Gcet

Shruti Patel | B.Tech | Computer Engineering | Gcet


📍 India
