import os
import requests
import json
import telebot

from varib import tele_bot_token, link
from search import get_wall_post

bot = telebot.TeleBot(tele_bot_token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет ✌️ ")

def test():
    bot.send_message(link)

bot.infinity_polling()