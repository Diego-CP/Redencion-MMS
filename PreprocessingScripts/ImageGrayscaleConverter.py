import os
from PIL import Image

# Set the directory path where your images are stored
folder_path = r'C:\TEC\Semestre8\Desarrollo\DeepGlobeDataset\test'
output_folder = r'C:\TEC\Semestre8\Desarrollo\DeepGlobeDataset\test_grayscale'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)
        
        # Open the image
        with Image.open(file_path) as img:
            # Convert the image to grayscale
            gray_img = img.convert('L')
            
            # Construct the output file path
            output_path = os.path.join(output_folder, filename)
            
            # Save the grayscale image
            gray_img.save(output_path)

print("Conversion complete. Grayscale images are saved in:", output_folder)
