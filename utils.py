import requests
import argparse
import os
from PIL import Image


def download_picture(folder, file_name, file_url, file_type):
    file_path = f"{folder}{file_name}{file_type}"
    response = requests.get(file_url, verify=False)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)


def edit_picture(folder):
    image = Image.open(f"{folder}")
    file_name = os.path.splitext(folder)[0]

    rgb_image = image.convert("RGB")
    rgb_image.thumbnail((1080, 1080))
    path = f"{file_name}.jpg"
    rgb_image.save(path, format="JPEG")
    return path


def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-p",
        "--path",
        type=str,
        help="Укажите путь для создания\\созданой папки : ",
        default="images/"
    )
    return parser
