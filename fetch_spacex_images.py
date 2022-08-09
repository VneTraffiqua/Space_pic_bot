import requests
from pathlib import Path
import argparse
import HelperScripts
import os
from dotenv import load_dotenv


def get_args():
    parser = argparse.ArgumentParser(
        description='Script to download images from the Spacex rocket launch'
    )
    parser.add_argument(
        'launch_id', nargs='?',
        default='latest',
        help='Spacex rocket launch id'
    )
    return parser.parse_args()


def get_url_pic_spacex(spacex_url):
    response = requests.get(
        f'{spacex_url}'
    )
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def main():
    load_dotenv()
    img_path = os.getenv('IMG_PATH')
    Path(f'{img_path}').mkdir(parents=True, exist_ok=True)
    launch_id = get_args().launch_id
    launch_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    for img_num, img_url in enumerate(get_url_pic_spacex(launch_url), 1):
        path = Path.cwd() / f'{img_path}' / \
               f'spacex{img_num}{HelperScripts.get_extension(img_url)}'
        HelperScripts.save_image(path, img_url)


if __name__ == '__main__':
    main()
