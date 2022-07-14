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
    return [i['url'] for i in response.json() if i['media_type'] == 'image']


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    start_date_apod = os.getenv('start_date_APOD')
    Path('./images').mkdir(parents=True, exist_ok=True)
    for img_num, APOD_url in enumerate(get_APOD(), 1):
        path = f'./images/NASA{img_num}{get_func.get_extension_file(APOD_url)}'
        get_func.get_images(path, APOD_url)