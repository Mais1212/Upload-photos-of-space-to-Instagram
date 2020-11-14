import requests
import main
from pathvalidate import sanitize_filename


def fetch_spacex_last_launch():
    response = requests.get("https://api.spacexdata.com/v3/launches").json()

    for launch in response:
        images = launch["links"]["flickr_images"]

        for url_imgae in enumerate(images):
            print(url_imgae)
            file_type = main.identify_extension(url_imgae[1])
            file_name = sanitize_filename(
                launch["mission_name"]) + str(url_imgae[0])
            print(file_name)
            main.donwload_img(file_name, url_imgae[1], file_type)


if __name__ == '__main__':
    fetch_spacex_last_launch()
    main.main()
