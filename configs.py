import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 28918271))
    API_HASH = os.environ.get("API_HASH", "29bf447b916a795191046a91317869fb")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7707522221:AAFEc5JiXCPydeA3bTN77a8L1M0IwtMgd-M")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQFqAQUAILF71ce55v3V4Q_RX28TKyzEz2D-B5HD0T6Q4mAuiNS1GKshZJUSfzKmGw00CqAuPQUxbOn_gxDC0qjyHTcuo30gVOuTbWL3AWnd6Z5Sef4lP_AhSxMhUuLjDNaGUHpZ0s3PBh6Z9cMXBmLMHbOj9jRHd9Tu8PfMHmTSJQ-t_uLJQSlNMmOORHD13tvMFWhBsO5NJqTvB00DclFyYRxZt5Y8L9oFajnDUBpgEAe2Q5JmUJtdUcNPsMfXa8FQ6fKlYSwXpHsCEUXoyDLiZTjcZb0DOl3Pa1uFuTTa1_R0bNSSQFB-hEcmoeuazY7YPXMelePqOulfAgGra_T3V1n-yQAAAAF24wVEAA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002471954376"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Misss_Lucy_bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "6692613520"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://sitaratoons:sitaratoons@cluster0.98nq3.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
    
    
🤖 My Name: <a href='https://youtube.com/@GreyMattersBot'>Link Search Bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='koyeb.com'>Koyeb</a>

👨‍💻 Created By: <a href='https://t.me/GreyMatter_Bot'>GreyMatter's Bot</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Creator : <a href='https://t.me/GreyMatter_Bot'>GreyMatter's Bot</a>
If You Want Your Own Bot Like This Then You Can Contact Our Creator.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @GreyMatter_Bots</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @GreyMatter_Bots</a></b>
"""

