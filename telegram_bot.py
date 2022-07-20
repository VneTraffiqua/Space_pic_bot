import telegram
import os
from dotenv import load_dotenv


load_dotenv()
tg_token = os.getenv('TELEGRAM_TOKEN')
bot = telegram.Bot(token=f'{tg_token}')
bot.send_document(chat_id=709161558, document=open('images/NASA2.jpg', 'rb'))


updates = bot.get_updates()
print([u.message.photo for u in updates if u.message.photo])
