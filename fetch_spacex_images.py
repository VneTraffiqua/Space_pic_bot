import requests
from pathlib import Path
import get_func
import argparse
import os


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('launch_id', nargs='?')
    return parser.parse_args()


def get_url_pic_spacex(spacex_url):
    response = requests.get(
        f'{spacex_url}'
    )
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


if __name__ == '__main__':
    img_path = os.getenv('IMG_PATH')
    Path(f'{img_path}').mkdir(parents=True, exist_ok=True)
    launch_id = get_args().launch_id
    if launch_id:
        url_launch = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    else:
        url_launch = 'https://api.spacexdata.com/v5/launches/latest'
    for img_num, img_url in enumerate(get_url_pic_spacex(url_launch), 1):
        path = f'./images/spacex{img_num}{get_func.get_extension(img_url)}'
        get_func.get_images(path, img_url)
