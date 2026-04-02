#!/usr/bin/env python3
"""
Main Training Pipeline
Runs the complete brain tumor detection pipeline.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from preprocess import get_data
from model import build_model, train_model, evaluate_model, plot_training_history, save_model

def main():
    print("=" * 60)
    print("Brain Tumor Detection - Training Pipeline")
    print("=" * 60)
    
    print("\n[1/5] Loading and preprocessing data...")
    X_train, X_test, y_train, y_test = get_data()
    print(f"Data loaded: {len(X_train)} training, {len(X_test)} testing samples")
    
    print("\n[2/5] Building CNN model...")
    model = build_model(input_shape=X_train[0].shape)
    
    print("\n[3/5] Training the model...")
    history, model = train_model(model, X_train, y_train, X_test, y_test, epochs=10)
    
    print("\n[4/5] Evaluating the model...")
    accuracy, cm = evaluate_model(model, X_test, y_test)
    
    print("\n[5/5] Saving the model...")
    model_path = save_model(model)
    
    plot_training_history(history)
    
    print("\n" + "=" * 60)
    print("Training Complete!")
    print(f"Test Accuracy: {accuracy:.4f}")
    print(f"Model saved to: {model_path}")
    print("=" * 60)
    
    return model, accuracy

if __name__ == "__main__":
    main()
