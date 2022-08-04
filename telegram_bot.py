import time
import telegram
import random
from pathlib import Path
import HelperScripts


def main():
    img_path = HelperScripts.get_global_variable('IMG_PATH')
    bot = telegram.Bot(
        token=HelperScripts.get_global_variable('TELEGRAM_TOKEN')
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
                    chat_id=HelperScripts.get_global_variable('TG_CHAT_ID'),
                    document=document
                )
            time.sleep(int(HelperScripts.get_global_variable('TIMER')))
        random.shuffle(img_names)


if __name__ == '__main__':
    main()
