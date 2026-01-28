import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# ---------- CONFIG ----------
MODEL_PATH = "signature_cnn_model.h5"
IMAGE_PATH = "test_single/sample.png"
IMG_SIZE = 128
# ----------------------------

# Load model
model = load_model(MODEL_PATH, compile=False)

# Load image in GRAYSCALE
img = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
if img is None:
    raise ValueError("Image not found!")

# Resize (MUST match training)
img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

# Normalize
img = img / 255.0

# Add channel + batch dimension
img = img.reshape(1, IMG_SIZE, IMG_SIZE, 1)

print("Input shape:", img.shape)  # 🔍 sanity check

# Prediction
prediction = model.predict(img, verbose=0)[0][0]

# Threshold
if prediction >= 0.5:
    result = "REAL SIGNATURE"
    confidence = prediction
else:
    result = "FORGED SIGNATURE"
    confidence = 1 - prediction

# Output
print("Prediction:", result)
print("Confidence:", round(confidence * 100, 2), "%")

# Display image
plt.imshow(img[0, :, :, 0], cmap="gray")
plt.title(f"{result} ({round(confidence * 100, 2)}%)")
plt.axis("off")
plt.show()
