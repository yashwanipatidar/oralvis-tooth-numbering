import os
import shutil
import random

# Set random seed for reproducibility
random.seed(42)

# Paths
base_dir = r'c:/Users/Lenovo/Downloads/oralvis'
images_dir = os.path.join(base_dir, 'images')
labels_dir = os.path.join(base_dir, 'labels')

splits = ['train', 'val', 'test']
split_ratio = [0.8, 0.1, 0.1]  # 80% train, 10% val, 10% test

# Create split directories if not exist
def make_dirs():
    for split in splits:
        os.makedirs(os.path.join(images_dir, split), exist_ok=True)
        os.makedirs(os.path.join(labels_dir, split), exist_ok=True)

# Get all image files
image_files = [f for f in os.listdir(images_dir) if f.lower().endswith('.jpg')]
image_files.sort()

# Shuffle and split
random.shuffle(image_files)
total = len(image_files)
train_end = int(split_ratio[0] * total)
val_end = train_end + int(split_ratio[1] * total)

train_files = image_files[:train_end]
val_files = image_files[train_end:val_end]
test_files = image_files[val_end:]

split_map = {'train': train_files, 'val': val_files, 'test': test_files}

make_dirs()

# Move files
def move_files(split, files):
    for img in files:
        label = img.replace('.jpg', '.txt')
        src_img = os.path.join(images_dir, img)
        src_label = os.path.join(labels_dir, label)
        dst_img = os.path.join(images_dir, split, img)
        dst_label = os.path.join(labels_dir, split, label)
        if os.path.exists(src_img) and os.path.exists(src_label):
            shutil.move(src_img, dst_img)
            shutil.move(src_label, dst_label)

for split, files in split_map.items():
    move_files(split, files)

print('Dataset split complete!')
