import requests
import os
from dotenv import load_dotenv
import get_func
from pathlib import Path


def get_EPIC_url():
    url1 = 'https://api.nasa.gov/EPIC/api/natural/images'
    settings = {
        'api_key': f'{nasa_token}',
        'start_date': f'{start_data_epic}'
    }
    response = requests.get(url1, params=settings)
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    start_data_epic = os.getenv('START_DATE_EPIC')
    img_path = os.getenv('IMG_PATH')
    Path(f'{img_path}').mkdir(parents=True, exist_ok=True)
    for img_num, EPIC_data in enumerate(get_EPIC_url(), 1):
        image_id = EPIC_data['image']
        image_date = EPIC_data['date'].split()[0].split('-')
        EPIC_url = f'https://api.nasa.gov/EPIC/archive/natural/' \
                   f'{image_date[0]}/{image_date[1]}/{image_date[2]}/' \
                   f'png/{image_id}.png'
        path = f'./images/NASA_EPIC_{img_num}.png'
        settings_epic_url = {
            'api_key': f'{nasa_token}',
        }
        get_func.get_images(path, EPIC_url, settings_epic_url)
