import telegram
import random
import argparse
from pathlib import Path
import HelperScripts


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('img_name', nargs='?')
    return parser.parse_args()


def main():
    img_name = get_args().img_name
    img_path = HelperScripts.get_global_variable('IMG_PATH')
    bot = telegram.Bot(
        token=HelperScripts.get_global_variable('TELEGRAM_TOKEN')
    )
    img_names = [
        img_name for img_name in HelperScripts.get_img_names(img_path)
    ]
    with open(Path.cwd() /
              f'{img_path}' /
              f'{img_name if img_name else random.choice(img_names)}', 'rb'
              ) as document:
        bot.send_document(
            chat_id=HelperScripts.get_global_variable('TG_CHAT_ID'),
            document=document
        )

if __name__ == '__main__':
    main()
