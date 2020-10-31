from pathlib import Path
from PIL import Image
from instabot import Bot
from dotenv import load_dotenv
import fnmatch
import os
import requests

url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
response_pic = requests.get(url)


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
    image_files = response["image_files"][-1]["file_url"]
    file_type = "." + image_files.split(".")[-1]
    donwload_img(id_img, image_files, file_type)


def donwload_img(name, file_url, file_type):
    file_path = "images/" + str(name)
    response = requests.get("https:" + file_url, verify=False)
    Path("images").mkdir(parents=True, exist_ok=True)
    with open(file_path + file_type, 'wb') as file:
        file.write(response.content)

    crop_picture(file_path, file_type)


def fetch_spacex_last_launch():
    numerate = 0
    response = requests.get("https://api.spacexdata.com/v3/launches").json()

    for s in response:
        images = s["links"]["flickr_images"]

        for img in images:
            numerate += 1

            response_img = requests.get(img)

            with open("images/spacex" + str(numerate) + ".jpg.", 'wb') as file:
                file.write(response_img.content)


def crop_picture(img_name, file_type):
    image = Image.open(img_name + file_type)

    rgb_image = image.convert("RGB")
    if rgb_image.size[1] > 1080:
        rgb_image.thumbnail((1079, 1079))

    rgb_image.thumbnail((1079, 1079))
    rgb_image.save(img_name + ".jpg", format="JPEG")


def upload_image(img_name):
    load_dotenv()
    login = os.getenv('INSTAGRAM_LOGIN')
    password = os.getenv('INSTAGRAM_PASSWORD')
    try:
        bot = Bot()
        bot.login(username=login, password=password)
        bot.upload_photo(img_name, caption=img_name)
    except Exception:
        print("Ошибка")

    if bot.api.last_response.status_code != 200:
        print(bot.api.last_response)


def remove_png():
    images_png = [file for file in os.listdir(
        "images") if not file.endswith(".jpg")]

    for image in images_png:
        os.remove(os.path.join("images", image))


def main():
    remove_png()
    listOfFiles = os.listdir('images')
    pattern = "*.jpg"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            upload_image("images/" + entry)


if __name__ == "__main__":
    main()
