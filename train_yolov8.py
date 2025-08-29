# train_yolov8.py
# OralVis Tooth Numbering YOLOv8 Training Script for Colab

# 1. Install Ultralytics YOLOv8
!pip install ultralytics

# 2. Import and check version
from ultralytics import YOLO
import ultralytics
print(ultralytics.__version__)

# 3. Set paths (update as needed)
DATA_YAML = '/content/data.yaml'  # Path to your data.yaml
MODEL = 'yolov8s.pt'              # Or yolov8n.pt, yolov8m.pt, etc.
EPOCHS = 100
IMG_SIZE = 640
PROJECT = '/content/oralvis_results'
NAME = 'yolov8s_fdi'

# 4. Train the model
model = YOLO(MODEL)
results = model.train(
    data=DATA_YAML,
    epochs=EPOCHS,
    imgsz=IMG_SIZE,
    batch=16,
    project=PROJECT,
    name=NAME,
    # Augmentation settings
    degrees=10,         # random rotation
    translate=0.1,      # random translation
    scale=0.5,          # random scaling
    shear=2,            # random shear
    perspective=0.001,  # random perspective
    flipud=0.5,         # vertical flip
    fliplr=0.5,         # horizontal flip
    mosaic=1.0,         # mosaic augmentation
    mixup=0.2,          # mixup augmentation
    hsv_h=0.015,        # HSV hue augmentation
    hsv_s=0.7,          # HSV saturation
    hsv_v=0.4           # HSV value
)

# 5. Evaluate on test set
metrics = model.val(data=DATA_YAML, split='test')

# 6. Plot training curves
results.plot()

# 7. Predict on test images and save results
model.predict(
    source='/content/dataset/images/test',  # Update path if needed
    save=True,
    conf=0.25,
    imgsz=IMG_SIZE,
    project=PROJECT,
    name='predictions'
)
