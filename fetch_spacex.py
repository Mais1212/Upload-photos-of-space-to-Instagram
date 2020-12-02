import utils
import requests
from pathvalidate import sanitize_filename


def fetch_spacex_last_launch():
    response = requests.get("https://api.spacexdata.com/v3/launches")
    response.raise_for_status()
    response_json = response.json()

    for launch in response_json:
        images = launch["links"]["flickr_images"]

        for url_imgae in enumerate(images):
            id_picture, url_imgae = url_imgae
            file_type = utils.identify_extension(url_imgae)
            file_name = sanitize_filename(
                f"{launch['mission_name']} - {id_picture}")
            utils.donwload_picture(file_name, url_imgae, file_type)


if __name__ == '__main__':
    try:
        fetch_spacex_last_launch()
    except requests.exceptions.HTTPError as erorr:
        print(erorr)
