#!/usr/bin/env python3
"""
Brain Tumor Detection - Prediction Script
Predicts whether a brain MRI image contains a tumor.
"""
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models', 'brain_tumor_model.keras')
IMG_SIZE = 224

def preprocess_image(image_path):
    """Preprocess a single image for prediction"""
    img = cv2.imread(image_path)
    
    if img is None:
        raise ValueError(f"Could not load image from {image_path}")
    
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)
    
    return img

def predict(image_path, model_path=MODEL_PATH):
    """Predict whether the image contains a tumor"""
    
    if not os.path.exists(model_path):
        print(f"Error: Model not found at {model_path}")
        print("Please train the model first using the Jupyter notebook.")
        return None
    
    model = load_model(model_path)
    
    img = preprocess_image(image_path)
    
    prediction = model.predict(img, verbose=0)[0][0]
    
    if prediction > 0.5:
        result = "Tumor Detected"
        confidence = prediction * 100
    else:
        result = "No Tumor"
        confidence = (1 - prediction) * 100
    
    print(f"\n{'='*50}")
    print(f"Brain Tumor Detection Result")
    print(f"{'='*50}")
    print(f"Image: {image_path}")
    print(f"Prediction: {result}")
    print(f"Confidence: {confidence:.2f}%")
    print(f"{'='*50}\n")
    
    return {
        'result': result,
        'confidence': confidence,
        'tumor_probability': float(prediction)
    }

def predict_batch(image_folder):
    """Predict multiple images from a folder"""
    
    if not os.path.exists(MODEL_PATH):
        print(f"Error: Model not found at {MODEL_PATH}")
        return None
    
    model = load_model(MODEL_PATH)
    
    image_files = []
    for ext in ['*.jpg', '*.jpeg', '*.png', '*.bmp']:
        image_files.extend(os.path.join(image_folder, ext))
    
    results = []
    for img_path in image_files:
        try:
            img = preprocess_image(img_path)
            prediction = model.predict(img, verbose=0)[0][0]
            
            result = "Tumor" if prediction > 0.5 else "No Tumor"
            results.append({
                'image': os.path.basename(img_path),
                'result': result,
                'confidence': prediction * 100 if prediction > 0.5 else (1 - prediction) * 100
            })
        except Exception as e:
            print(f"Error processing {img_path}: {e}")
    
    return results

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python predict.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    predict(image_path)
