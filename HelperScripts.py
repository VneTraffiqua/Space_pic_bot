import requests
import urllib.parse
import os


def get_extension(user_url):
    parsed_url = urllib.parse.urlsplit(user_url)
    link, extension = os.path.splitext(parsed_url.path)
    return extension


def get_img_names(path):
    for img_name in os.listdir(path):
        if os.path.isfile(os.path.join(path, img_name)):
            yield img_name


def save_image(file_path, images_url, settings=None):
    response = requests.get(images_url, params=settings)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)
