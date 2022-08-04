import requests
from pathlib import Path
import HelperScripts


def get_epic_url():
    url1 = 'https://api.nasa.gov/EPIC/api/natural/images'
    settings = {
        'api_key': HelperScripts.get_global_variable('NASA_TOKEN'),
        'start_date': HelperScripts.get_global_variable('START_DATE_EPIC')
    }
    response = requests.get(url1, params=settings)
    response.raise_for_status()
    return response.json()


def main():
    img_path = HelperScripts.get_global_variable('IMG_PATH')
    Path(f'{img_path}').mkdir(parents=True, exist_ok=True)
    for img_num, EPIC_data in enumerate(get_epic_url(), 1):
        image_id = EPIC_data['image']
        image_date = EPIC_data['date'].split()[0].split('-')
        epic_url = f'https://api.nasa.gov/EPIC/archive/natural/' \
                   f'{image_date[0]}/{image_date[1]}/{image_date[2]}/' \
                   f'png/{image_id}.png'
        path = Path.cwd() / f'{img_path}' / f'NASA_EPIC_{img_num}.png'
        settings_epic_url = {
            'api_key': HelperScripts.get_global_variable('NASA_TOKEN'),
        }
        HelperScripts.get_images(path, epic_url, settings_epic_url)


if __name__ == '__main__':
    main()
