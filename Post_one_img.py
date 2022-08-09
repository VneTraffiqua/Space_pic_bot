import telegram
import random
import argparse
from pathlib import Path
import HelperScripts
import os
from dotenv import load_dotenv


def get_args():
    parser = argparse.ArgumentParser(
        description='Post_one_img.py publish specified image or random image.'
    )
    parser.add_argument('img_name', nargs='?', help='Enter a image name')
    return parser.parse_args()


def main():
    load_dotenv()
    img_path = os.getenv('IMG_PATH')
    img_name = get_args().img_name
    bot = telegram.Bot(
        token=os.getenv('TELEGRAM_TOKEN')
    )
    img_names = [
        img_name for img_name in HelperScripts.get_img_names(img_path)
    ]
    image_path = Path.cwd() / f'{img_path}' / \
           f'{img_name if img_name else random.choice(img_names)}'
    with open(image_path, 'rb') as document:
        bot.send_document(
            chat_id=os.getenv('TG_CHAT_ID'),
            document=document
        )


if __name__ == '__main__':
    main()
