import os
import numpy as np
import cv2
from collections import Counter
from tqdm import tqdm


def deepglobe_classes():
    """DeepGlobe class names for external use."""
    return [
        'urban_land', 'agriculture_land', 'rangeland', 'forest_land', 'water',
        'barren_land', 'unknown'
    ]


def calculate_class_weights(mask_dir, num_classes):
    # Initialize a Counter to count the frequency of each class
    class_counts = Counter()

    # Loop over all mask files in the directory
    for mask_file in tqdm(os.listdir(mask_dir)):
        if mask_file.endswith('_mask.png'):
            # Read the segmentation mask
            mask_path = os.path.join(mask_dir, mask_file)
            mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

            # Flatten the mask to a 1D array and update class_counts
            class_counts.update(mask.flatten())

    # Get the total number of pixels
    total_pixels = sum(class_counts.values())

    # Calculate class weights
    class_weights = {cls: total_pixels /
                     count for cls, count in class_counts.items()}

    # Create a list of class weights in the order of class indices
    class_weights_list = [class_weights.get(i, 0) for i in range(num_classes)]

    return class_weights_list


mask_dir = 'C:/Users/salva/Documents/Git Repos/Redencion-MMS/data/deepglobe/ann_dir/train'

# Number of classes in the DeepGlobe dataset
class_names = deepglobe_classes()
num_classes = len(class_names)

# Calculate class weights
class_weights_list = calculate_class_weights(mask_dir, num_classes)

print(f"Class Weights: {class_weights_list}")
