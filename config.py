# (c) Seyori
# A Part of MegaDL-Bot <https://github.com/seyori-eth-h4xer/MegaDL-Bot>


import os

class Config:
    API_ID = int(os.environ.get("API_ID", 22419004))
    API_HASH = os.environ.get("API_HASH", "34982b52c4a83c2af3ce8f4fe12fe4e1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8129468158:AAFAutSObPvN6cTyk5ZeCqOTzC3IHEegFOM")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    TG_MAX_SIZE = 2040108421
    OWNER_ID = int(os.environ.get("OWNER_ID", 6742022802))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001907672237"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)


class TEXT:
  ABOUT = """
🤖 **Name:** {bot_name}

📝 **Language:** [Python](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted On:** [Heroku](https://heroku.com)

🧑‍💻 **Developer:** [Safone](https://t.me/s3yori)
"""

  HELP_USER = """
This is **{bot_name}**

This Bot Can Download Files & Videos From Mega Links & Upload To Telegram. Just Send Any Mega.nz Link & See The Magic. You Can Also Add or Change Caption: Just Select An Uploaded File/ Video or Forward Me Any Telegram File & Then Write The Text You Want To Be Caption On The File As A Reply To That File & The Text You Wrote Will Be Attached As Caption 😁! 

**Made With ❤️ By @noob_je ! 👑**
"""

  START_TEXT = """
👋🏻 **Hi** {user_mention},

I'm **{bot_name}**
I Can Download Files & Videos From Mega.nz Links & Upload To Telegram. Please Check Help To Learn More 😉!

**Maintained By: {bot_owner}**❤️!
"""
