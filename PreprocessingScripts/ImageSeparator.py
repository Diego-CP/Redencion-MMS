import os
import shutil

# Define the source directory containing the images
source_dir = r'C:\TEC\Semestre8\Desarrollo\DeepGlobeDataset\train'

# Define the target directories for jpg and png images
jpg_dir = os.path.join(source_dir, 'jpg_images')
png_dir = os.path.join(source_dir, 'png_images')

# Create target directories if they do not exist
os.makedirs(jpg_dir, exist_ok=True)
os.makedirs(png_dir, exist_ok=True)

# Iterate through files in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith('.jpg'):
        shutil.move(os.path.join(source_dir, filename), os.path.join(jpg_dir, filename))
    elif filename.endswith('.png'):
        shutil.move(os.path.join(source_dir, filename), os.path.join(png_dir, filename))

print("Images have been separated into 'jpg_images' and 'png_images' folders.")
