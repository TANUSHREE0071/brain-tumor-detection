# Brain Tumor Detection Project

End-to-end CNN-based brain tumor detection system for Kali Linux.

## Project Structure

```
tumour/
├── tumour_env/              # Virtual environment
├── data/                    # Dataset folder
│   ├── Training/
│   │   ├── yes/            # Images with tumor
│   │   └── no/             # Images without tumor
│   └── Testing/
│       ├── yes/
│       └── no/
├── models/                  # Saved models
├── brain_tumor_detection.ipynb  # Main Jupyter notebook
├── preprocess.py           # Data preprocessing
├── model.py                # CNN model definition
├── train.py                # Training pipeline
├── predict.py              # Prediction script
├── download_dataset.py     # Dataset downloader
├── launch.py               # Auto-launch script
└── README.md
```

## Quick Start

### 1. Activate Virtual Environment
```bash
source tumour_env/bin/activate
```

### 2. Download Dataset
Download from Kaggle: https://www.kaggle.com/datasets/rashikrahmanpritam/Brain-Tumor-Classification-Image-Dataset

Extract to the `data/` folder maintaining the Training/Testing structure.

### 3. Launch Jupyter Notebook
```bash
jupyter notebook brain_tumor_detection.ipynb
```

Or use the auto-launch script:
```bash
python launch.py
```

## Requirements

- Python 3.13+
- TensorFlow 2.21+
- Keras 3.13+
- OpenCV
- NumPy
- Matplotlib
- scikit-learn

All requirements are installed in the virtual environment.

## Usage

### Training
Open `brain_tumor_detection.ipynb` and run all cells to:
1. Load and preprocess data
2. Build CNN model
3. Train the model
4. Evaluate and view results

### Prediction
```bash
python predict.py <image_path>
```

## Model Architecture

- 3 Conv2D layers (32, 64, 128 filters)
- MaxPooling after each conv layer
- Flatten layer
- Dense(128) + Dropout(0.5)
- Dense(64) + Dropout(0.3)
- Output: Dense(1, sigmoid)

## Results

- Test accuracy and loss printed
- Training history graphs saved
- Confusion matrix visualization
- Trained model saved to models/brain_tumor_model.keras

## Notes

- Image size: 224x224
- Uses binary crossentropy loss
- Adam optimizer with learning rate 0.001
- Early stopping to prevent overfitting
