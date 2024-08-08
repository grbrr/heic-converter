import os
import glob
from tqdm import tqdm
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

# Create output directory if it doesn't exist
if not os.path.exists("./output"):
    os.makedirs("./output")

# Get all HEIC files in the input directory
heic_files = glob.glob("./input/*.heic")

# Convert all HEIC files to PNG with a progress bar
for file in tqdm(heic_files, desc="Converting HEIC to PNG"):
    image = Image.open(file)
    new_file = os.path.basename(file).replace(".heic", ".png")
    image.save(f"./output/{new_file}", "PNG")

print("All files converted successfully")