import os
import requests
import urllib3
import utils

from pathlib import Path


def download_collections(folder):
    collections = ["holiday_cards", "wallpaper",
                   "spacecraft", "news", "printshop", "stsci_gallery"]
    for collection in collections:
        response = requests.get(
            f"http://hubblesite.org/api/v3/images/{collection}")
        response.raise_for_status()

        for picture in response.json():
            file_id = picture["id"]
            download_hubblesite_img(folder, file_id)


def download_hubblesite_img(folder, file_id):
    response = requests.get(
        f"http://hubblesite.org/api/v3/image/{file_id}")
    response.raise_for_status()
    file_url = f"https:{response.json()['image_files'][-1]['file_url']}"
    file_type = os.path.splitext(file_url)[1]
    utils.download_picture(folder, file_id, file_url, file_type)


if __name__ == "__main__":
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    try:
        parser = utils.create_parser()
        namespace = parser.parse_args()
        directory = namespace.path
        Path(directory).mkdir(parents=True, exist_ok=True)

        download_collections(directory)
    except requests.exceptions.HTTPError as erorr:
        print(f"Произошла ошибка : \n{erorr}")
