import os
import fnmatch
import utils
from instabot import Bot
from dotenv import load_dotenv


def upload_image(img_name):
    load_dotenv()
    login = os.getenv('INSTAGRAM_LOGIN')
    password = os.getenv('INSTAGRAM_PASSWORD')
    bot = Bot()
    bot.login(username=login, password=password)
    bot.upload_photo(img_name, caption=img_name)


def main():
    parser = utils.create_parser()
    namespace = parser.parse_args()
    directory = namespace.path
    print(directory)

    files = os.listdir('images')
    expansion = "*.jpg"
    for entry in files:
        print(entry)
        if fnmatch.fnmatch(entry, expansion):
            try:
                upload_image(directory + entry)
            except Exception:
                print(f"Картинка {entry} не скачалась")
                continue


if __name__ == "__main__":
    main()
