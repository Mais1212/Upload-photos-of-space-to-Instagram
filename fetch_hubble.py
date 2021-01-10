import utils
import requests


def colletion(file_path):
    colletions = ["holiday_cards", "wallpaper",
                  "spacecraft", "news", "printshop", "stsci_gallery"]
    for colletion in colletions:
        response = requests.get(
            f"http://hubblesite.org/api/v3/images/{colletion}")
        response.raise_for_status()

        for picture in response.json():
            file_id = picture["id"]
            donwload_hubblesite_img(file_path, file_id)


def donwload_hubblesite_img(file_path, file_id):
    response = requests.get(
        f"http://hubblesite.org/api/v3/image/{str(file_id)}").json()
    file_url = f"https:{response['image_files'][-1]['file_url']}"
    file_type = utils.identify_extension(file_url)
    utils.donwload_picture(file_path, file_id, file_url, file_type)


if __name__ == "__main__":
    try:
        parser = utils.create_parser()
        namespace = parser.parse_args()
        directory = namespace.path
        print(directory)

        colletion(directory)
    except requests.exceptions.HTTPError as erorr:
        print(f"Произошла ошибка : \n{erorr}")
