import time
import telegram
import os
from dotenv import load_dotenv
import random
import get_func


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.getenv('TELEGRAM_TOKEN')
    img_path = os.getenv('IMG_PATH')
    bot = telegram.Bot(token=f'{tg_token}')
    img_names = [i for i in get_func.get_img_names(img_path)]
    while True:
        for img_name in get_func.get_img_names(img_path):
            bot.send_document(
                chat_id=os.getenv('CHAT_ID'),
                document=open(f'{img_path}/{img_name}', 'rb')
            )
            time.sleep(int(os.getenv('TIMER')))
        random.shuffle(img_names)
