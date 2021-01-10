import utils
import requests
import os
from pathvalidate import sanitize_filename


def fetch_spacex_last_launch(file_path):
    response = requests.get("https://api.spacexdata.com/v3/launches")
    response.raise_for_status()
    response_json = response.json()

    for launch in response_json:
        images = launch["links"]["flickr_images"]

        for file_url in enumerate(images):
            file_id, file_url = file_url
            file_type = utils.identify_extension(file_url)
            file_name = sanitize_filename(
                f"{launch['mission_name']} - {file_id}")
            utils.donwload_picture(file_path, file_name, file_url, file_type)


if __name__ == '__main__':
    try:
        parser = utils.create_parser()
        namespace = parser.parse_args()
        directory = os.path.join(namespace.path)
        fetch_spacex_last_launch(directory)

    except requests.exceptions.HTTPError as erorr:
        print(erorr)
