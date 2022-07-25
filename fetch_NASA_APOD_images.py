import requests
from dotenv import load_dotenv
from pathlib import Path
import get_func
import os


def get_APOD():
    url_nasa = 'https://api.nasa.gov/planetary/apod'
    settings = {
        'api_key': f'{nasa_token}',
        'start_date': f'{start_date_apod}'
    }
    response = requests.get(url_nasa, params=settings)
    response.raise_for_status()
    return [data['url'] for data in response.json() 
            if data['media_type'] == 'image'
            ]


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    img_path = os.getenv('IMG_PATH')
    start_date_apod = os.getenv('START_DATE_APOD')
    Path(f'{img_path}').mkdir(parents=True, exist_ok=True)
    for img_num, APOD_url in enumerate(get_APOD(), 1):
        path = f'{img_path}/NASA{img_num}{get_func.get_extension(APOD_url)}'
        get_func.get_images(path, APOD_url)
