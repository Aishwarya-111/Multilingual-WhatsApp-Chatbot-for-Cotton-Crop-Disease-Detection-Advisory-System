import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# Define custom layers to silently handle version-specific attribute mismatches
class PatchedDense(keras.layers.Dense):
    def __init__(self, *args, **kwargs):
        # Ignore quantization_config which might not be supported in this Keras version
        kwargs.pop('quantization_config', None)
        super().__init__(*args, **kwargs)

class PatchedInputLayer(keras.layers.InputLayer):
    def __init__(self, *args, **kwargs):
        # Normalize batch_shape vs shape vs batch_input_shape
        batch_shape = kwargs.pop('batch_shape', kwargs.pop('batch_input_shape', None))
        if batch_shape is not None and 'shape' not in kwargs:
            # Keras 3 expects 'shape' (without the batch dimension)
            kwargs['shape'] = batch_shape[1:]
        super().__init__(*args, **kwargs)

def load_robust_model(model_path):
    print(f"Loading {model_path} with compatibility patches...")
    # Map the standard names to our patched versions
    custom_objects = {
        'Dense': PatchedDense,
        'InputLayer': PatchedInputLayer
    }
    # Load without compiling to avoid optimizer attribute errors
    return keras.models.load_model(model_path, custom_objects=custom_objects, compile=False)

def evaluate_model():
    model_path = os.path.join("model", "best_model.h5")
    test_data_dir = r"dataset\final_dataset\test"
    
    if not os.path.exists(model_path):
        print(f"Error: Model not found at {model_path}")
        return
    if not os.path.exists(test_data_dir):
        print(f"Error: Test dataset folder not found at {test_data_dir}")
        return

    try:
        model = load_robust_model(model_path)
        print("Model loaded successfully!")
    except Exception as e:
        print(f"FAILED TO LOAD MODEL: {e}")
        return
    
    # Standard image parameters
    img_size = 224
    batch_size = 16

    print("Preparing Test Data Generator...")
    test_datagen = keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
    test_generator = test_datagen.flow_from_directory(
        test_data_dir,
        target_size=(img_size, img_size),
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=False 
    )

    if test_generator.samples == 0:
        print("ERROR: No images found in test directory.")
        return

    print(f"Running predictions on {test_generator.samples} test images...")
    predictions = model.predict(test_generator, steps=len(test_generator))
    y_pred = np.argmax(predictions, axis=1)
    y_true = test_generator.classes
    class_names = list(test_generator.class_indices.keys())

    # 1. Overall Accuracy
    acc = accuracy_score(y_true, y_pred)
    print("\n" + "="*40)
    print(f"OVERALL ACCURACY: {acc * 100:.2f}%")
    print("="*40 + "\n")

    # 2. Classification Report (Precision, Recall, F1)
    report = classification_report(y_true, y_pred, target_names=class_names)
    print("Full Classification Report:")
    print(report)
    
    with open("classification_report.txt", "w") as f:
        f.write(f"Accuracy: {acc * 100:.2f}%\n\nDetailed Report:\n")
        f.write(report)

    # 3. Confusion Matrix Visualization
    print("Generating Confusion Matrix Plot...")
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(12, 10))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
    plt.title('Disease Detection: Confusion Matrix', fontsize=16)
    plt.ylabel('Ground Truth (Actual)', fontsize=12)
    plt.xlabel('AI Prediction', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('confusion_matrix.png', dpi=300)
    
    print("\nSUCCESS: Evaluation metrics generated!")
    print("- Results table: classification_report.txt")
    print("- Visual plot: confusion_matrix.png")

if __name__ == "__main__":
    evaluate_model()
