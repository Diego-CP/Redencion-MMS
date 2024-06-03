import os
import cv2
import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms


class CustomImageDataset(Dataset):
    def __init__(self, img_dir, transform=None):
        self.img_dir = img_dir
        self.transform = transform
        self.image_files = [f for f in os.listdir(
            img_dir) if os.path.isfile(os.path.join(img_dir, f))]

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.image_files[idx])
        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if self.transform:
            image = self.transform(image)
        return image


# Path to your image directory (para el mio funcionó poniendo el path completo desde C:)
img_dir = 'C:/Users/salva/Documents/Git Repos/Redencion-MMS/data/deepglobe/img_dir/train'

# Define the transformation to convert images to tensors
transform = transforms.Compose([
    transforms.ToTensor()
])

# Create the dataset and dataloader
dataset = CustomImageDataset(img_dir, transform=transform)
dataloader = DataLoader(dataset, batch_size=1, shuffle=False)

# Initialize variables to accumulate pixel values
mean = 0.0
std = 0.0
nb_samples = 0

# Iterate over the dataset
for data in dataloader:
    data = data.view(data.size(0), data.size(1), -1)
    mean += data.mean(2).sum(0)
    std += data.std(2).sum(0)
    nb_samples += data.size(0)

mean /= nb_samples
std /= nb_samples

print(f"Mean: {mean}")
print(f"Standard Deviation: {std}")
