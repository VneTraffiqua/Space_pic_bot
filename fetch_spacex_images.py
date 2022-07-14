import requests
from pathlib import Path
import main
import argparse


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
    Path('./images').mkdir(parents=True, exist_ok=True)
    launch_id = get_args().launch_id
    if launch_id:
        url_launch = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    else:
        url_launch = 'https://api.spacexdata.com/v5/launches/latest'
    for img_num, img_url in enumerate(get_url_pic_spacex(url_launch), 1):
        path = f'./images/spacex{img_num}{main.get_extension_file(img_url)}'
        main.get_images(path, img_url)
