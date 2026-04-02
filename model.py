#!/usr/bin/env python3
"""
CNN Model for Brain Tumor Detection
Builds, trains, and evaluates a convolutional neural network.
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')
os.makedirs(MODEL_PATH, exist_ok=True)

def build_model(input_shape=(224, 224, 3)):
    """Build CNN model for brain tumor detection"""
    
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D((2, 2)),
        
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(64, activation='relu'),
        Dropout(0.3),
        
        Dense(1, activation='sigmoid')
    ])
    
    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    model.summary()
    return model

def train_model(model, X_train, y_train, X_test, y_test, epochs=10, batch_size=32):
    """Train the CNN model"""
    
    early_stopping = EarlyStopping(
        monitor='val_loss',
        patience=3,
        restore_best_weights=True
    )
    
    print("\nTraining the model...")
    history = model.fit(
        X_train, y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_split=0.1,
        callbacks=[early_stopping],
        verbose=1
    )
    
    return history, model

def evaluate_model(model, X_test, y_test):
    """Evaluate the model and show results"""
    
    print("\nEvaluating model...")
    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
    print(f"Test Loss: {loss:.4f}")
    print(f"Test Accuracy: {accuracy:.4f}")
    
    y_pred = (model.predict(X_test, verbose=0) > 0.5).astype(int).flatten()
    
    cm = confusion_matrix(y_test, y_pred)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['No Tumor', 'Tumor'],
                yticklabels=['No Tumor', 'Tumor'])
    plt.title('Confusion Matrix')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.tight_layout()
    plt.savefig(os.path.join(MODEL_PATH, 'confusion_matrix.png'), dpi=150)
    plt.close()
    print(f"Confusion matrix saved to {MODEL_PATH}/confusion_matrix.png")
    
    return accuracy, cm

def plot_training_history(history):
    """Plot training and validation accuracy/loss"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    ax1.plot(history.history['accuracy'], label='Training Accuracy')
    ax1.plot(history.history['val_accuracy'], label='Validation Accuracy')
    ax1.set_title('Model Accuracy')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Accuracy')
    ax1.legend()
    
    ax2.plot(history.history['loss'], label='Training Loss')
    ax2.plot(history.history['val_loss'], label='Validation Loss')
    ax2.set_title('Model Loss')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Loss')
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig(os.path.join(MODEL_PATH, 'training_history.png'), dpi=150)
    plt.close()
    print(f"Training history plot saved to {MODEL_PATH}/training_history.png")

def save_model(model):
    """Save the trained model"""
    model_path = os.path.join(MODEL_PATH, 'brain_tumor_model.keras')
    model.save(model_path)
    print(f"Model saved to {model_path}")
    return model_path

def load_model(model_path=None):
    """Load a trained model"""
    from tensorflow.keras.models import load_model
    
    if model_path is None:
        model_path = os.path.join(MODEL_PATH, 'brain_tumor_model.keras')
    
    if not os.path.exists(model_path):
        print(f"Model not found at {model_path}")
        return None
    
    model = load_model(model_path)
    print(f"Model loaded from {model_path}")
    return model

if __name__ == "__main__":
    print("Testing model build...")
    model = build_model()
    print("Model built successfully!")
