import requests
import urllib.parse
import os


def get_extension_file(user_url):
    parsed_url = urllib.parse.urlsplit(user_url)
    return os.path.splitext(parsed_url.path)[1]


def get_images(file_path, images_url, settings=None):
    response = requests.get(images_url, params=settings)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)

