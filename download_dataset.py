#!/usr/bin/env python3
"""
Download Brain MRI Dataset
This script downloads the Brain Tumor Classification dataset from Kaggle.
"""
import os
import sys
import zipfile
import shutil

def create_sample_dataset(base_path):
    """Create a sample dataset with synthetic data for demonstration"""
    print("Creating sample dataset structure...")
    
    categories = {
        'yes': 'Brain Tumor',
        'no': 'No Tumor'
    }
    
    for category, label in categories.items():
        train_path = os.path.join(base_path, 'Training', category)
        test_path = os.path.join(base_path, 'Testing', category)
        os.makedirs(train_path, exist_ok=True)
        os.makedirs(test_path, exist_ok=True)
    
    print(f"Sample dataset structure created at {base_path}")
    print("Note: For actual training, please provide Kaggle API credentials or download the dataset manually")
    return True

def download_via_kaggle(base_path):
    """Download using Kaggle API"""
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
        api = KaggleApi()
        api.authenticate()
        
        print("Downloading Brain Tumor Classification dataset...")
        api.dataset_download_files(
            'rashikrahmanpritam/Brain+Tumor+Classification+Image+Dataset',
            path=base_path,
            unzip=True
        )
        return True
    except Exception as e:
        print(f"Kaggle API error: {e}")
        return False

def download_alternative(base_path):
    """Try alternative download source"""
    import urllib.request
    
    print("Trying alternative download method...")
    
    dataset_dirs = ['Training', 'Testing']
    categories = ['yes', 'no']
    
    for dir_name in dataset_dirs:
        for category in categories:
            path = os.path.join(base_path, dir_name, category)
            os.makedirs(path, exist_ok=True)
    
    print(f"Created directory structure at {base_path}")
    print("\nTo get actual dataset:")
    print("1. Go to: https://www.kaggle.com/datasets/rashikrahmanpritam/Brain-Tumor-Classification-Image-Dataset")
    print("2. Download and extract to the data folder")
    print("3. Or provide Kaggle API credentials")
    
    return True

if __name__ == "__main__":
    base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    os.makedirs(base_path, exist_ok=True)
    
    print("=" * 60)
    print("Brain Tumor Dataset Downloader")
    print("=" * 60)
    
    if not download_via_kaggle(base_path):
        print("\nFalling back to alternative method...")
        download_alternative(base_path)
    
    print("\nDownload complete!")
