import main
import requests


def colletion():
    colletions = ["holiday_cards", "wallpaper",
                  "spacecraft", "news", "printshop", "stsci_gallery"]
    for colletion in colletions:
        response = requests.get(
            f"http://hubblesite.org/api/v3/images/{colletion}").json()
        response.raise_for_status()

        for picture in response:
            id_img = picture["id"]
            donwload_hubblesite_img(id_img)


def donwload_hubblesite_img(id_img):
    response = requests.get(
        f"http://hubblesite.org/api/v3/image/{str(id_img)}").json()
    response.raise_for_status()
    image_url = f"https:{response['image_files'][-1]['file_url']}"
    file_type = main.identify_extension(image_url)
    main.donwload_img(id_img, image_url, file_type)


if __name__ == "__main__":
    try:
        colletion()
    except requests.exceptions.HTTPError:
        print("python")
