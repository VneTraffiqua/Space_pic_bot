import requests
from pathlib import Path


def get_images(file_path, images_url):
    response = requests.get(images_url)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)


def get_url_pic_spacex(spacex_url):
    response = requests.get(
        f'{spacex_url}'
    )
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


if __name__ == '__main__':
    Path('./images').mkdir(parents=True, exist_ok=True)
    #
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    #get_images(path, url)
    #print(get_url_pic_spacex(url))
    for img_num, spacex_url in enumerate(get_url_pic_spacex(url), 1):
        print(img_num, spacex_url)
        path = f'./images/spacex{img_num}.jpeg'
        get_images(path, spacex_url)