# Load .env
from dotenv import load_dotenv
from os import getenv
import threading
import telebot
load_dotenv()


bot_token = getenv("BOT_TOKEN")
bot = telebot.TeleBot(bot_token)
@bot.message_handler(commands=['start', 'help', 'ayuda'])
def cmd_start(message):
    bot.reply_to(message, "Aloha, en que te puedo ayudar? ⚡")

@bot.message_handler(content_types=['text'])
def bot_mensajes_texto(message):
    print(message.from_user.username)
    white_list = ["rcanelav", "AnitaPunetes"]
    if message.from_user.username not in white_list:
        dispatch_unknown_user(message)
        return
    
    # If the user is AnitaPunetes, append the 
    bot.reply_to(message, "Hola, " + message.from_user.username + " ⚡")
    voice_note = open("src/resources/voice/notaAntia.ogg", "rb")
    bot.send_voice(message.chat.id, voice_note)


def start_bot():
    bot.infinity_polling()

def dispatch_unknown_user(message):
    voice_note = open("src/resources/voice/notacapuyo.ogg", "rb")
    bot.reply_to(message, f"Lo siento, {message.from_user.first_name} {message.from_user.last_name} no tienes permisos para usar este bot ⚡")
    bot.send_voice(message.chat.id, voice_note)

if __name__ == '__main__':
    print("Bot started")
    bot_listener = threading.Thread(name="bot_rayci", target=start_bot)
    bot_listener.start()
