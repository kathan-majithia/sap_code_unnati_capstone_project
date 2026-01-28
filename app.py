from flask import Flask, render_template, request, jsonify
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

os.makedirs("uploads", exist_ok=True)

# Load model once
# model = load_model("signature_cnn_model.h5", compile=False)
model = load_model("signature_model_safe",compile=False)
IMG_SIZE = 128

def preprocess_image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = img.reshape(1, IMG_SIZE, IMG_SIZE, 1)
    return img

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "img1" not in request.files or "img2" not in request.files:
        return jsonify({"error": "Two images required"})

    img1 = request.files["img1"]
    img2 = request.files["img2"]

    path1 = os.path.join(app.config["UPLOAD_FOLDER"], img1.filename)
    path2 = os.path.join(app.config["UPLOAD_FOLDER"], img2.filename)

    img1.save(path1)
    img2.save(path2)

    p1 = model.predict(preprocess_image(path1), verbose=0)[0][0]
    p2 = model.predict(preprocess_image(path2), verbose=0)[0][0]

    if p1 > p2:
        real = "Image 1"
        forged = "Image 2"
    else:
        real = "Image 2"
        forged = "Image 1"

    return jsonify({
        "img1_conf": round(p1 * 100, 2),
        "img2_conf": round(p2 * 100, 2),
        "real": real,
        "forged": forged
    })

if __name__ == "__main__":
    app.run(debug=True)
