import os
import requests
import urllib3
import utils

from pathlib import Path
from pathvalidate import sanitize_filename


def fetch_spacex_last_launch(folder):
    response = requests.get("https://api.spacexdata.com/v3/launches/latest")
    response.raise_for_status()

    images = response.json()["links"]["flickr_images"]
    if images == []:
        print("Кажется, картинок нет ;(")

    for file_id, file_url in enumerate(images):
        file_type = os.path.splitext(file_url)[1]
        file_name = sanitize_filename(
            f"{response.json()['mission_name']} - {file_id}")
        utils.download_picture(folder, file_name, file_url, file_type)


if __name__ == '__main__':
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    try:
        parser = utils.create_parser()
        namespace = parser.parse_args()
        directory = namespace.path
        Path(directory).mkdir(parents=True, exist_ok=True)
        fetch_spacex_last_launch(directory)

    except requests.exceptions.HTTPError as erorr:
        print(erorr)
