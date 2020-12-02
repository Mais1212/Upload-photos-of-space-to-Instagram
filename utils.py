import os
import requests
from PIL import Image
from pathlib import Path


def donwload_picture(name, file_url, file_type):
    file_path = f"images/{str(name)}"
    response = requests.get(file_url, verify=False)
    response.raise_for_status()
    Path("images").mkdir(parents=True, exist_ok=True)
    with open(file_path + file_type, 'wb') as file:
        file.write(response.content)

    crop_picture(file_path, file_type)


def crop_picture(img_name, file_type):
    image = Image.open(img_name + file_type)

    rgb_image = image.convert("RGB")
    rgb_image.thumbnail((1080, 1080))
    rgb_image.save(f"{img_name}.jpg", format="JPEG")


def identify_extension(url):
    file_type = os.path.splitext(url)[1]
    return file_type
