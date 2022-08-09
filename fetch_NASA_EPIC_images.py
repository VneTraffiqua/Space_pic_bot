import requests
from pathlib import Path
import HelperScripts
import os
from dotenv import load_dotenv


def get_epic_url(api_key, start_date):
    url1 = 'https://api.nasa.gov/EPIC/api/natural/images'
    settings = {
        'api_key': api_key,
        'start_date': start_date
    }
    response = requests.get(url1, params=settings)
    response.raise_for_status()
    return response.json()


def main():
    load_dotenv()
    img_path = os.getenv('IMG_PATH')
    epic_start_date = os.getenv('START_DATE_EPIC')
    nasa_token = os.getenv('NASA_TOKEN')
    Path(f'{img_path}').mkdir(parents=True, exist_ok=True)
    for img_num, EPIC_data in enumerate(
            get_epic_url(nasa_token, epic_start_date), 1
    ):
        image_id = EPIC_data['image']
        year, month, day = EPIC_data['date'].split()[0].split('-')
        epic_url = f'https://api.nasa.gov/EPIC/archive/natural/' \
                   f'{year}/{month}/{day}/' \
                   f'png/{image_id}.png'
        path = Path.cwd() / f'{img_path}' / f'NASA_EPIC_{img_num}.png'
        settings_epic_url = {
            'api_key': nasa_token,
        }
        HelperScripts.save_image(path, epic_url, settings_epic_url)


if __name__ == '__main__':
    main()
