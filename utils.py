import requests
import argparse
import os
from PIL import Image
import urllib3


def download_picture(file_path, file_name, file_url, file_type):
    # path_name = f"{file_path}{file_name}"
    # print(f"{path_name} | {path_name_type}")
    path_name_type = f"{file_path}{file_name}{file_type}"
    response = requests.get(file_url, verify=False)
    response.raise_for_status()
    with open(path_name_type, 'wb') as file:
        file.write(response.content)


def crop_picture(file_path):
    image = Image.open(f"{file_path}")
    file_name = os.path.splitext(file_path)[0]

    rgb_image = image.convert("RGB")
    rgb_image.thumbnail((1080, 1080))
    rgb_image.save(f"{file_name}.jpg", format="JPEG")


def create_parser():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-p",
        "--path",
        type=str,
        help="Укажите путь для создания\\созданой папки : ",
        default="images/"
    )
    return parser
