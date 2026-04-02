#!/usr/bin/env python3
"""
Data Preprocessing for Brain Tumor Detection
Loads, preprocesses, and splits the dataset.
"""
import os
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
import glob

IMG_SIZE = 224
DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def load_and_preprocess_data():
    """Load and preprocess brain MRI images"""
    
    training_path = os.path.join(DATA_PATH, 'Training')
    testing_path = os.path.join(DATA_PATH, 'Testing')
    
    def load_images_from_folder(folder_path, label):
        images = []
        labels = []
        
        if not os.path.exists(folder_path):
            print(f"Warning: {folder_path} does not exist")
            return images, labels
            
        categories = ['yes', 'no']
        
        for category in categories:
            category_path = os.path.join(folder_path, category)
            if not os.path.exists(category_path):
                continue
                
            files = glob.glob(os.path.join(category_path, '*.*'))
            print(f"Loading {len(files)} images from {category_path}")
            
            for img_file in files:
                try:
                    img = cv2.imread(img_file)
                    if img is not None:
                        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
                        img = img.astype('float32') / 255.0
                        images.append(img)
                        labels.append(1 if category == 'yes' else 0)
                except Exception as e:
                    print(f"Error loading {img_file}: {e}")
        
        return images, labels
    
    print("Loading training data...")
    train_images, train_labels = load_images_from_folder(training_path, 'train')
    
    print("Loading testing data...")
    test_images, test_labels = load_images_from_folder(testing_path, 'test')
    
    all_images = train_images + test_images
    all_labels = train_labels + test_labels
    
    if len(all_images) == 0:
        print("No images found. Creating sample data...")
        return create_sample_data()
    
    X = np.array(all_images)
    y = np.array(all_labels)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")
    print(f"Image shape: {X_train[0].shape}")
    
    return X_train, X_test, y_train, y_test

def create_sample_data():
    """Create sample data for demonstration"""
    print("Creating sample dataset...")
    
    np.random.seed(42)
    
    n_samples = 100
    IMG_SIZE = 224
    
    X_train = np.random.rand(n_samples, IMG_SIZE, IMG_SIZE, 3).astype('float32')
    X_test = np.random.rand(n_samples // 4, IMG_SIZE, IMG_SIZE, 3).astype('float32')
    y_train = np.random.randint(0, 2, n_samples)
    y_test = np.random.randint(0, 2, n_samples // 4)
    
    print(f"Sample training samples: {len(X_train)}")
    print(f"Sample testing samples: {len(X_test)}")
    
    return X_train, X_test, y_train, y_test

def get_data():
    """Public function to get preprocessed data"""
    return load_and_preprocess_data()

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = get_data()
    print(f"\nData loaded successfully!")
    print(f"X_train shape: {X_train.shape}")
    print(f"X_test shape: {X_test.shape}")
    print(f"y_train distribution: {np.bincount(y_train)}")
    print(f"y_test distribution: {np.bincount(y_test)}")
