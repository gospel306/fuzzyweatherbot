
from fuzzyweather.text import *


class Commands:
    def __init__(self):
        pass

    def command_start(self, bot, update):
        user_name = update.message.from_user.first_name

        bot.sendMessage(
            update.message.chat_id,
            text=TEXT_START.format(
                user_name=user_name, bot_name=bot.name))
        bot.sendMessage(
            update.message.chat_id,
            text=TEXT_HELP)

    def command_help(self, bot, update):
        bot.sendMessage(
            update.message.chat_id,
            text=TEXT_HELP)
