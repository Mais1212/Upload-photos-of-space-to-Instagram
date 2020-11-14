import main
import requests


def colletion():
    colletions = ["holiday_cards", "wallpaper",
                  "spacecraft", "news", "printshop", "stsci_gallery"]
    for colletion in colletions:
        response = requests.get(
            "http://hubblesite.org/api/v3/images/" + colletion).json()

        for elem in response:
            id_img = elem["id"]
            donwload_hubblesite_img(id_img)


def donwload_hubblesite_img(id_img):
    response = requests.get(
        "http://hubblesite.org/api/v3/image/" + str(id_img)).json()
    image_url = "https:" + response["image_files"][-1]["file_url"]
    file_type = main.identify_extension(image_url)
    main.donwload_img(id_img, image_url, file_type)


if __name__ == "__main__":
    colletion()
    main.main()
