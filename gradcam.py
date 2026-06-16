import numpy as np
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load model
model = load_model("best_model.h5")

# Class names (same order as training)
class_names = [
    "bacterial_blight",
    "curl_virus",
    "healthy_leaf",
    "herbicidegrowth_damage",
    "leaf_hopper_jassids",
    "leaf_reddning",
    "leaf_variegation"
]

# Load image
img_path = "test.jpg"
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Predict class
preds = model.predict(img_array)
class_index = np.argmax(preds[0])
print("Prediction:", class_names[class_index])

# Get last convolution layer
last_conv_layer = model.get_layer("Conv_1")

# Create Grad-CAM model
grad_model = tf.keras.models.Model(
    inputs=model.inputs,
    outputs=[last_conv_layer.output, model.output]
)

# Compute gradients
with tf.GradientTape() as tape:
    conv_outputs, predictions = grad_model(img_array)
    loss = predictions[:, class_index]

grads = tape.gradient(loss, conv_outputs)

# Compute channel-wise mean
pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

# Multiply gradients with feature maps
conv_outputs = conv_outputs[0]
heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]
heatmap = tf.squeeze(heatmap)

# Convert to numpy safely
heatmap = heatmap.numpy()

# Normalize heatmap
heatmap = np.maximum(heatmap, 0)
heatmap /= np.max(heatmap) + 1e-8

# Read original image
img_original = cv2.imread(img_path)
img_original = cv2.resize(img_original, (224, 224))

# Resize heatmap
heatmap = cv2.resize(heatmap, (224, 224))

# Convert to color map
heatmap = np.uint8(255 * heatmap)
heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)

# Overlay heatmap on image
superimposed_img = cv2.addWeighted(img_original, 0.6, heatmap, 0.4, 0)

# Show result
plt.imshow(cv2.cvtColor(superimposed_img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title("Grad-CAM Heatmap")
plt.show()