import requests
from pathlib import Path
import HelperScripts
import os
from dotenv import load_dotenv


def get_apod(api_key, start_date):
    url_nasa = 'https://api.nasa.gov/planetary/apod'
    settings = {
        'api_key': api_key,
        'start_date': start_date
    }
    response = requests.get(url_nasa, params=settings)
    response.raise_for_status()
    return [row['url'] for row in response.json()
            if row['media_type'] == 'image'
            ]


def main():
    load_dotenv()
    img_path = os.getenv('IMG_PATH')
    apod_start_date = os.getenv('START_DATE_APOD')
    nasa_token = os.getenv('NASA_TOKEN')
    Path(f'{img_path}').mkdir(parents=True, exist_ok=True)
    for img_num, apod_url in enumerate(
            get_apod(nasa_token, apod_start_date), 1
    ):
        path = Path.cwd() / f'{img_path}' / \
               f'NASA{img_num}{HelperScripts.get_extension(apod_url)}'
        HelperScripts.save_images(path, apod_url)


if __name__ == '__main__':
    main()
