import telegram
import os
from dotenv import load_dotenv
import random
import argparse
import get_func
from pathlib import Path



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('img_name', nargs='?')
    return parser.parse_args()


if __name__ == '__main__':
    img_name = get_args().img_name
    load_dotenv()
    tg_token = os.getenv('TELEGRAM_TOKEN')
    img_path = os.getenv('IMG_PATH')
    bot = telegram.Bot(token=tg_token)
    img_names = [i for i in get_func.get_img_names(img_path)]
    if img_name:
        bot.send_document(
            chat_id=os.getenv('CHAT_ID'),
            document=open(Path.cwd() / f'{img_path}' / f'{img_name}', 'rb')
        )
    else:
        bot.send_document(
            chat_id=os.getenv('CHAT_ID'),
            document=open(
                Path.cwd() /
                f'{img_path}' /
                f'{random.choice(img_names)}',
                'rb'
            )
        )
