# OralVis Tooth Numbering Detection

This project trains a YOLOv8 model to detect and number teeth in dental panoramic images using the FDI system.

## Project Structure
- `images/` and `labels/`: Raw dataset (split into train/val/test)
- `data.yaml`: YOLO dataset config
- `train_yolov8.py`: Training script
- `postprocess_fdi.py`: Post-processing for anatomical FDI assignment
- `requirements.txt`: Python dependencies
- `Dockerfile`: For containerized training
- `cleanup.py`: Removes unwanted files
- `merge_images_labels.py`: Merges images and labels into single folders per split

## Setup

### 1. Python Virtual Environment
```
python -m venv oralvis_env
oralvis_env\Scripts\activate
pip install -r requirements.txt
```

### 2. Data Preparation
- Place your images and labels in the correct folders.
- Use `split_dataset.py` to split into train/val/test.
- Use `merge_images_labels.py` if you want images and labels together per split.

### 3. Training
```
python train_yolov8.py
```

Or with Docker:
```
docker build -t oralvis-yolo .
docker run --gpus all oralvis-yolo
```

## Post-Processing
- Use `postprocess_fdi.py` to assign FDI numbers anatomically to predictions.

## Results & Evaluation
- Training logs, weights, and metrics are saved automatically.
- Evaluate using the built-in YOLOv8 validation and test scripts.

## Environment
- Python 3.10+
- See `requirements.txt` for dependencies

## Citation
OralVis – Redefining Oral Health

---
For questions or issues, please open an issue or contact the maintainer.
"# oralvis-tooth-numbering" 
