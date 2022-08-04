import requests
from pathlib import Path
import argparse
import HelperScripts


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('launch_id', nargs='?', default='latest')
    return parser.parse_args()


def get_url_pic_spacex(spacex_url):
    response = requests.get(
        f'{spacex_url}'
    )
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def main():
    img_path = HelperScripts.get_global_variable('IMG_PATH')
    Path(f'{img_path}').mkdir(parents=True, exist_ok=True)
    launch_id = get_args().launch_id
    url_launch = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    for img_num, img_url in enumerate(get_url_pic_spacex(url_launch), 1):
        path = Path.cwd() / f'{img_path}' / \
               f'spacex{img_num}{HelperScripts.get_extension(img_url)}'
        HelperScripts.get_images(path, img_url)


if __name__ == '__main__':
    main()
