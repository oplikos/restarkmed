import os
from PIL import Image

# Paths
source_folder = "menuPic"
output_folder = "menuPic_optimized"
scale_percent = 70  # Resize to 50% of original size

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through files in source folder
for filename in os.listdir(source_folder):
    if filename.lower().endswith(".png"):
        input_path = os.path.join(source_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Open image
        with Image.open(input_path) as img:
            # Calculate new size
            new_width = int(img.width * scale_percent / 100)
            new_height = int(img.height * scale_percent / 100)
            resized_img = img.resize((new_width, new_height), Image.LANCZOS)

            # Save resized image
            resized_img.save(output_path, optimize=True)

print("✅ All images resized and saved to:", output_folder)
