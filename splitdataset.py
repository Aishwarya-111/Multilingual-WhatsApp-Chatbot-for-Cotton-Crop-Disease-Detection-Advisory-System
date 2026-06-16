import os
import shutil
import random

# Your dataset path (input)
source_dir = r"E:\New folder\Minorprojectedit\dataset\Augmented Dataset"

# New dataset path (output)
base_dir = r"E:\New folder\Minorprojectedit\dataset\final_dataset"

train_ratio = 0.7
val_ratio = 0.15

# Create folders
for split in ['train', 'val', 'test']:
    os.makedirs(os.path.join(base_dir, split), exist_ok=True)

# Loop through each class
for class_name in os.listdir(source_dir):
    class_path = os.path.join(source_dir, class_name)

    if not os.path.isdir(class_path):
        continue

    images = os.listdir(class_path)
    random.shuffle(images)

    train_split = int(len(images) * train_ratio)
    val_split = int(len(images) * (train_ratio + val_ratio))

    train_imgs = images[:train_split]
    val_imgs = images[train_split:val_split]
    test_imgs = images[val_split:]

    for split, split_imgs in zip(
        ['train', 'val', 'test'],
        [train_imgs, val_imgs, test_imgs]
    ):
        split_path = os.path.join(base_dir, split, class_name)
        os.makedirs(split_path, exist_ok=True)

        for img in split_imgs:
            src = os.path.join(class_path, img)
            dst = os.path.join(split_path, img)
            shutil.copyfile(src, dst)

print("Dataset split completed!")