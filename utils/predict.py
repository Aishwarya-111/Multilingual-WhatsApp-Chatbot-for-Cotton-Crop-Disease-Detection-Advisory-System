import numpy as np
import os
import keras
from keras.models import load_model
from keras.preprocessing import image
from keras.layers import Dense

# --- WORKAROUND FOR KERAS 3 LOADING BUG ---
class FixedDense(Dense):
    """
    Fixed Dense layer that ignores 'quantization_config' if present in the model file.
    This is necessary because some Keras versions save this field but fail to load it.
    """
    def __init__(self, *args, **kwargs):
        kwargs.pop('quantization_config', None)
        super().__init__(*args, **kwargs)

# ------------------------------------------

# Define constants
IMG_SIZE = (224, 224)
MODEL_PATH = os.path.join("model", "best_model.h5")
CONFIDENCE_THRESHOLD = 0.85

# Class names mapping
class_names = [
    "bacterial_blight",
    "curl_virus",
    "healthy_leaf",
    "herbicidegrowth_damage",
    "leaf_hopper_jassids",
    "leaf_reddning",
    "leaf_variegation"
]

# Load model once at module level
model = None

def get_model():
    global model
    if model is None:
        custom_objects = {"Dense": FixedDense}
        model = load_model(MODEL_PATH, custom_objects=custom_objects)
    return model

def predict_disease(img_path):
    """
    Predicts the cotton leaf disease from an image.
    Returns: top_class, confidence, top_2_results, is_reliable
    """
    try:
        # Load and preprocess image
        img = image.load_img(img_path, target_size=IMG_SIZE)
        img_array = image.img_to_array(img)
        img_array = img_array / 255.0  # Normalize
        img_array = np.expand_dims(img_array, axis=0)

        # Get prediction
        model = get_model()
        predictions = model.predict(img_array)[0]
        
        # Get top indices and confidence
        top_indices = np.argsort(predictions)[::-1][:2]
        top_class = class_names[top_indices[0]]
        confidence = float(predictions[top_indices[0]])
        
        top_2_results = [
            {"class": class_names[idx], "score": float(predictions[idx])}
            for idx in top_indices
        ]
        
        is_reliable = confidence >= CONFIDENCE_THRESHOLD
        
        return top_class, confidence, top_2_results, is_reliable
        
    except Exception as e:
        print(f"Error in prediction: {e}")
        return None, 0, [], False
