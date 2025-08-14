import os
from PIL import Image
input_folder = "input_folder"     
output_folder = "images_output"   
new_size = (800, 800)             
output_format = "JPEG"            
os.makedirs(output_folder, exist_ok=True)
valid_extensions = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"}
for filename in os.listdir(input_folder):
    file_ext = os.path.splitext(filename)[1].lower()
    if file_ext in valid_extensions:
        input_path = os.path.join(input_folder, filename)
        with Image.open(input_path) as img:
            img = img.resize(new_size)
            output_filename = os.path.splitext(filename)[0] + "." + output_format.lower()
            output_path = os.path.join(output_folder, output_filename)
            img.save(output_path, output_format)
            print(f" Resized and saved: {output_filename}")
print(" Batch resizing complete!")