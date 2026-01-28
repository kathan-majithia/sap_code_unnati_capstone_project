import tensorflow as tf
import numpy as np

print("TensorFlow Version:", tf.__version__)

# Simple dataset
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)

# Model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=[1])
])

model.compile(optimizer='adam', loss='mse')

# Train model
model.fit(X, y, epochs=100, verbose=0)

# Test
prediction = model.predict(np.array([[6]], dtype=float))
print("Prediction for 6:", prediction)
