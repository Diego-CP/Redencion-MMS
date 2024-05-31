import os
from PIL import Image

# Define the directory containing the images and the target size
input_dir = r"C:\TEC\Semestre8\Desarrollo\DeepGlobeDataset\test_grayscale"
output_dir = r"C:\TEC\Semestre8\Desarrollo\DeepGlobeDataset\test_reduced"
target_size = (512, 512)

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through all the files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        img_path = os.path.join(input_dir, filename)
        img = Image.open(img_path)
        
        # Check if the image is 2448x2448
        if img.size == (2448, 2448):
            # Resize the image
            img_resized = img.resize(target_size, Image.LANCZOS)
            
            # Save the resized image to the output directory
            output_path = os.path.join(output_dir, filename)
            img_resized.save(output_path)
            #print(f"Resized and saved {filename} to {output_dir}")

print("Resizing complete.")
