import os
import pydicom
from PIL import Image
import numpy as np

def convert_ima_to_jpg(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for file_name in os.listdir(input_dir):
        if file_name.endswith('.IMA'):
            file_path = os.path.join(input_dir, file_name)

            dicom_data = pydicom.dcmread(file_path)

            pixel_array = dicom_data.pixel_array

            pixel_array = (pixel_array - pixel_array.min()) / (pixel_array.max() - pixel_array.min()) * 255
            pixel_array = pixel_array.astype(np.uint8)

            image = Image.fromarray(pixel_array)

            output_file_path = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}.jpg")

            image.save(output_file_path)

            print(f"Converted {file_name} to {output_file_path}")

input_directory = 'ima_imgs'
output_directory = 'jpg_imgs'

convert_ima_to_jpg(input_directory, output_directory)
