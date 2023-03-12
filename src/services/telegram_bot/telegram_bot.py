import telebot
from dotenv import load_dotenv
from os import getenv

from utils import white_list
load_dotenv()

class telegram_bot:
    __instance = None
    bot_token = getenv("BOT_TOKEN")
    bot = telebot.TeleBot(bot_token)
    @staticmethod
    def get_instance():
        if telegram_bot.__instance == None:
            telegram_bot()
        return telegram_bot.__instance
    
    def __init__(self):
        if telegram_bot.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            telegram_bot.__instance = telebot.TeleBot(telegram_bot.bot_token)
            print("Telegram bot initialized")
# bot_token = getenv("BOT_TOKEN")
# bot = telebot.TeleBot(bot_token)
# @bot.message_handler(content_types=['text'])
# def bot_mensajes_texto(message):
#     print(message.from_user.username)
#     users_white_list = white_list.get_users()
#     if message.from_user.username not in users_white_list:
#         dispatch_unknown_user(message)
#         return

#     # If the message is a url, extract the title
#     if "http" in message.text:
#         # get the title from the previsually extracted url
#         save_url(message.text)

# def dispatch_unknown_user(message):
#     voice_note = open("src/resources/voice/notacapuyo.ogg", "rb")
#     bot.reply_to(message, f"Lo siento, {message.from_user.first_name} {message.from_user.last_name} no tienes permisos para usar este bot ⚡")
#     bot.send_voice(message.chat.id, voice_note)