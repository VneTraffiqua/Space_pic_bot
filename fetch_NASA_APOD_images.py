import requests
from pathlib import Path
import HelperScripts


def get_apod():
    url_nasa = 'https://api.nasa.gov/planetary/apod'
    settings = {
        'api_key': HelperScripts.get_global_variable('NASA_TOKEN'),
        'start_date': HelperScripts.get_global_variable('START_DATE_APOD')
    }
    response = requests.get(url_nasa, params=settings)
    response.raise_for_status()
    return [row['url'] for row in response.json()
            if row['media_type'] == 'image'
            ]


def main():
    img_path = HelperScripts.get_global_variable('IMG_PATH')
    Path(f'{img_path}').mkdir(parents=True, exist_ok=True)
    for img_num, apod_url in enumerate(get_apod(), 1):
        path = Path.cwd() / f'{img_path}' / \
               f'NASA{img_num}{HelperScripts.get_extension(apod_url)}'
        HelperScripts.get_images(path, apod_url)


if __name__ == '__main__':
    main()
