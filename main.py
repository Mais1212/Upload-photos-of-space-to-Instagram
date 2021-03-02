import os
import fnmatch
import utils
from instabot import Bot
from dotenv import load_dotenv


def upload_image(img_name, login, password):
    bot = Bot()
    bot.login(username=login, password=password)
    bot.upload_photo(img_name, caption=img_name)


def main():
    load_dotenv()
    login = os.getenv('INSTAGRAM_LOGIN')
    password = os.getenv('INSTAGRAM_PASSWORD')

    parser = utils.create_parser()
    namespace = parser.parse_args()
    directory = namespace.path

    try:
        files = os.listdir(directory)
    except FileNotFoundError:
        print(f"Возможно вы указали неверный путь к папке,\
 или не указали указали на конце пути '\\'")
        exit()

    extension = "*.jpg"
    for entry in files:
        file_path = f"{directory}{entry}"
        try:
            print(entry)
            utils.crop_picture(file_path)
            if fnmatch.fnmatch(entry, extension):
                pass
                upload_image(f"{directory} {entry}", login, password)
        except FileNotFoundError:
            print(f"Возможно вы указали неверный путь к папке, или не указали \
указали на конце \\")
            continue


if __name__ == "__main__":
    main()
