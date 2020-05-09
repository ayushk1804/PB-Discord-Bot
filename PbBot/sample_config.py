import os

class Config(object):
    # get a token from Discord Developer portal
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = int(os.environ.get("AUTH_CHANNEL", -100))
    # to specify delete message duration and log channel for bot
    Delete_after_duration = float(os.environ.get("Delete_after_duration", 10.0))
    LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", -100))
