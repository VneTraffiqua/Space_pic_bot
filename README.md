# Space_pic_bot
This project collects space images NASA and SpaceX then publishes them on a telegram-channel.

## How to install?

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```pip install -r requirements.txt```

Recommended to use [virtualenv/venv](https://docs.python.org/3/library/venv.html) for isolate the project
## Launch.

Generate NASA API Key [api.nasa.gov](https://api.nasa.gov/).

Register telegram bot and get Telegram token.([how to register a bot?
](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html))

Get your telegram chat ID: write `/start` to @getmyid_bot in telegram.

#### Added to `.env` file:
- `NASA_TOKEN` -  NASA token to work with the API
- `START_DATE_APOD` - the start of a date range, when requesting date for a range of  APOD images
- `START_DATE_EPIC` - the start of a date range, when requesting date for a range of  EPIC images
- `TELEGRAM_TOKEN` - yelegram token to work with the API
- `CHAT_ID` - your user ID in telegram
- `TIMER` - a timer for delayed posts.(measured in seconds)
- `IMG_PATH` - path to images folder

#### Collect images of space:

Run `fetch_spacex_images.py` with the optional parameter "id", to download images from the rocket launch by a given id.
Run without the optional parameter to download i,ages from the latest rocket launch.

Run `fetch_NASA_APOD_images.py` to download NASA APOD.

Run `fetch_NASA_EPIC_images.py` to download NASA EPIC.

#### Work with telegram-bot:
Run `telegram_bot.py` to publish images from a collection(`IMG_PATH`) after the specified time(`TIMER`)

Run `Post_one_img.py` with the optional parameter "image name" to publish specified image.
Run `Post_one_img.py` without the optional parameter to publish random image from collection

=========================================================

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org).
 

