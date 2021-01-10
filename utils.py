import os
import requests
import argparse
from PIL import Image
from pathlib import Path


def donwload_picture(file_path, file_name, file_url, file_type):
    path_name = f"{file_path}{str(file_name)}"
    path_name_type = f"{file_path}{str(file_name)}{file_type}"
    response = requests.get(file_url, verify=False)
    response.raise_for_status()
    Path(file_path).mkdir(parents=True, exist_ok=True)
    with open(path_name_type, 'wb') as file:
        file.write(response.content)

    crop_picture(path_name, file_type)


def crop_picture(file_path, file_type):
    image = Image.open(file_path + file_type)

    rgb_image = image.convert("RGB")
    rgb_image.thumbnail((1080, 1080))
    rgb_image.save(f"{file_path}.jpg", format="JPEG")


def identify_extension(url):
    file_type = os.path.splitext(url)[1]
    return file_type


def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-p",
        "--path",
        type=str,
        help="Укажите путь до файла : ",
        default="1/2/3/"
    )
    return parser
