import time
import telegram
import random
from pathlib import Path
import HelperScripts
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    img_path = os.getenv('IMG_PATH')
    bot = telegram.Bot(
        token=os.getenv('TELEGRAM_TOKEN')
    )
    img_names = [
        img_name for img_name in HelperScripts.get_img_names(img_path)
    ]
    while True:
        for img_name in img_names:
            with open(
                    Path.cwd() / f'{img_path}' / f'{img_name}', 'rb'
            ) as document:
                bot.send_document(
                    chat_id=os.getenv('TG_CHAT_ID'),
                    document=document
                )
            time.sleep(int(os.getenv('TIMER')))
        random.shuffle(img_names)


if __name__ == '__main__':
    main()
