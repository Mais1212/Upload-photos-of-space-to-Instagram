import requests
from PIL import Image
from pathlib import Path
from instabot import Bot
from dotenv import load_dotenv
import fnmatch
import os


def identify_extension(url):
    file_type = os.path.splitext(url)[1]
    return file_type


def donwload_img(name, file_url, file_type):
    file_path = f"images/{str(name)}"
    response = requests.get(file_url, verify=False)
    response.raise_for_status()
    Path("images").mkdir(parents=True, exist_ok=True)
    with open(file_path + file_type, 'wb') as file:
        file.write(response.content)

    crop_picture(file_path, file_type)


def crop_picture(img_name, file_type):
    image = Image.open(img_name + file_type)

    rgb_image = image.convert("RGB")
    rgb_image.thumbnail((1080, 1080))
    rgb_image.save(f"{img_name}.jpg", format="JPEG")


def upload_image(img_name):
    load_dotenv()
    login = os.getenv('INSTAGRAM_LOGIN')
    password = os.getenv('INSTAGRAM_PASSWORD')
    bot = Bot()
    bot.login(username=login, password=password)
    bot.upload_photo(img_name, caption=img_name)


def main():
    files = os.listdir('images')
    expansion = "*.jpg"
    for entry in files:
        print(entry)
        if fnmatch.fnmatch(entry, expansion):
            try:
                upload_image(f"images/{entry}")
            except Exception:
                print(f"Картинка {entry} не скачалась")
                continue


if __name__ == "__main__":
    main()
