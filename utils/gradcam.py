# Grad-CAM XAI Module
import numpy as np
import tensorflow as tf
import cv2
import os
from keras.preprocessing import image
import keras

# Define constants
IMG_SIZE = (224, 224)
LAST_CONV_LAYER_NAME = "Conv_1"
OUTPUT_DIR = os.path.join("static", "gradcam_outputs")

def generate_gradcam(model, img_path, class_index, output_filename):
    """
    Generates a Grad-CAM heatmap for a given image and class index.
    Saves the output to static/gradcam_outputs/
    Returns the path to the saved heatmap.
    """
    try:
        # 1. Preprocess image
        img = image.load_img(img_path, target_size=IMG_SIZE)
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # 2. Create a model that maps input to last conv layer and output
        grad_model = keras.models.Model(
            inputs=model.inputs,
            outputs=[model.get_layer(LAST_CONV_LAYER_NAME).output, model.output]
        )

        # 3. Compute gradients
        with tf.GradientTape() as tape:
            conv_outputs, predictions = grad_model(img_array)
            loss = predictions[:, class_index]

        grads = tape.gradient(loss, conv_outputs)

        # 4. Global Average Pooling of gradients
        pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

        # 5. Multiply each channel in the feature map by "how important it is"
        conv_outputs = conv_outputs[0]
        heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]
        heatmap = tf.squeeze(heatmap)

        # 6. Normalize the heatmap
        heatmap = tf.maximum(heatmap, 0)
        heatmap /= tf.reduce_max(heatmap) + 1e-8
        heatmap = heatmap.numpy()

        # 7. Superimpose heatmap on original image
        img_original = cv2.imread(img_path)
        img_original = cv2.resize(img_original, IMG_SIZE)
        
        # Resize heatmap to match image size
        heatmap_resized = cv2.resize(heatmap, IMG_SIZE)
        heatmap_colored = np.uint8(255 * heatmap_resized)
        heatmap_colored = cv2.applyColorMap(heatmap_colored, cv2.COLORMAP_JET)

        # Combine
        superimposed_img = cv2.addWeighted(img_original, 0.6, heatmap_colored, 0.4, 0)

        # 8. Save result
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
            
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        cv2.imwrite(output_path, superimposed_img)
        
        return output_path

    except Exception as e:
        print(f"Error generating Grad-CAM: {e}")
        return None
