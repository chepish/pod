import os
import requests
import json
import telebot

from varib import tele_bot_token, link, search_done, group_names
from search import get_wall_post

bot = telebot.TeleBot(tele_bot_token)

@bot.message_handler(commands=['start'])
def start_message(message):
    print()
    for gm in group_names:
        get_wall_post(gm)
    for l in link:
        bot.send_message(message.chat.id, f"{l}")

bot.infinity_polling()