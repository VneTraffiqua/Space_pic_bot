import time
import telegram
import os
from dotenv import load_dotenv
import random
import get_func
from pathlib import Path



if __name__ == '__main__':
    load_dotenv()
    tg_token = os.getenv('TELEGRAM_TOKEN')
    img_path = os.getenv('IMG_PATH')
    bot = telegram.Bot(token=tg_token)
    img_names = [i for i in get_func.get_img_names(img_path)]
    while True:
        for img_name in get_func.get_img_names(img_path):
            bot.send_document(
                chat_id=os.getenv('CHAT_ID'),
                document=open(Path.cwd() / f'{img_path}' / f'{img_name}', 'rb')
            )
            time.sleep(int(os.getenv('TIMER')))
        random.shuffle(img_names)
