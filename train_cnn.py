import tensorflow as tf
from tensorflow.keras import layers, models

# -----------------------------
# CONFIG
# -----------------------------
IMG_SIZE = (128, 128)
BATCH_SIZE = 16
EPOCHS = 10

TRAIN_DIR = "dataset/train"
TEST_DIR = "dataset/test"

# -----------------------------
# LOAD DATA
# -----------------------------
train_ds = tf.keras.utils.image_dataset_from_directory(
    TRAIN_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    color_mode="grayscale",
    label_mode="binary"
)

test_ds = tf.keras.utils.image_dataset_from_directory(
    TEST_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    color_mode="grayscale",
    label_mode="binary"
)

# -----------------------------
# NORMALIZE DATA
# -----------------------------
normalization = layers.Rescaling(1./255)

train_ds = train_ds.map(lambda x, y: (normalization(x), y))
test_ds = test_ds.map(lambda x, y: (normalization(x), y))

# Improve performance
train_ds = train_ds.cache().shuffle(1000).prefetch(tf.data.AUTOTUNE)
test_ds = test_ds.cache().prefetch(tf.data.AUTOTUNE)

# -----------------------------
# CNN MODEL
# -----------------------------
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

    layers.Dense(1, activation='sigmoid')  # Binary classification
])

# -----------------------------
# COMPILE MODEL
# -----------------------------
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.summary()

# -----------------------------
# TRAIN MODEL
# -----------------------------
history = model.fit(
    train_ds,
    validation_data=test_ds,
    epochs=EPOCHS
)

# -----------------------------
# EVALUATE
# -----------------------------
loss, acc = model.evaluate(test_ds)
print(f"Test Accuracy: {acc * 100:.2f}%")

# -----------------------------
# SAVE MODEL
# -----------------------------
model.save("signature_cnn_model.h5")
print("✅ Model saved as signature_cnn_model.h5")
