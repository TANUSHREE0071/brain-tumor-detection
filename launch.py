#!/usr/bin/env python3
"""
Auto-setup and Launch Script
Automatically sets up the environment and launches Jupyter notebook.
"""
import os
import sys
import subprocess

def main():
    print("=" * 70)
    print("BRAIN TUMOR DETECTION - AUTOMATIC SETUP")
    print("=" * 70)
    
    project_dir = "/home/sn1per/Desktop/Projects/tumour"
    os.chdir(project_dir)
    
    print("\n[1/4] Creating sample dataset structure...")
    create_dataset_structure()
    
    print("\n[2/4] Creating models directory...")
    os.makedirs("models", exist_ok=True)
    
    print("\n[3/4] Verifying Jupyter installation...")
    check_jupyter()
    
    print("\n[4/4] Launching Jupyter Notebook...")
    launch_jupyter()

def create_dataset_structure():
    """Create the dataset directory structure"""
    categories = ['yes', 'no']
    
    for split in ['Training', 'Testing']:
        for category in categories:
            path = os.path.join('data', split, category)
            os.makedirs(path, exist_ok=True)
    
    print("Dataset structure created at: data/Training and data/Testing")
    print("Note: Place your Kaggle dataset here or use the notebook to download")

def check_jupyter():
    """Check if Jupyter is available"""
    try:
        result = subprocess.run(
            ['which', 'jupyter'],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print("Warning: Jupyter not found in PATH")
    except:
        pass

def launch_jupyter():
    """Launch Jupyter notebook"""
    print("\n" + "=" * 70)
    print("Launching Jupyter Notebook...")
    print("=" * 70)
    print("\nThe notebook will open in your browser.")
    print("File: brain_tumor_detection.ipynb")
    print("\nTo run from terminal:")
    print("  source tumour_env/bin/activate")
    print("  jupyter notebook brain_tumor_detection.ipynb")
    print("=" * 70 + "\n")
    
    try:
        subprocess.run(
            ['jupyter', 'notebook', 'brain_tumor_detection.ipynb'],
            cwd=os.getcwd()
        )
    except Exception as e:
        print(f"Error launching Jupyter: {e}")
        print("Please run manually: jupyter notebook brain_tumor_detection.ipynb")

if __name__ == "__main__":
    main()
