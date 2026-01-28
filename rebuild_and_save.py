import tensorflow as tf
from tensorflow.keras import layers, models

IMG_SIZE = (128, 128)

# 🔁 Rebuild SAME architecture
model = models.Sequential([
    layers.Input(shape=(128, 128, 1)),

    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D(),

    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(),

    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(),

    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),

    layers.Dense(1, activation='sigmoid')
])

# ⚠️ Load weights ONLY
model.load_weights("signature_cnn_model.h5")

# ✅ Save in SAFE format
model.save("signature_model_safe")

print("✅ Model rebuilt and saved safely")
