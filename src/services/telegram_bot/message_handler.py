from services.telegram_bot.telegram_bot import telegram_bot
from services.notion.save_new_url import save_url
from utils import white_list
import telebot

bot = telegram_bot.get_instance()
@bot.message_handler(content_types=['text'])
def bot_mensajes_texto(message):
    print(message.from_user.username)
    users_white_list = white_list.get_users()
    if message.from_user.username not in users_white_list:
        dispatch_unknown_user(message)
        return

    # If the message is a url, extract the title
    if "http" in message.text:
        # get the title from the previsually extracted url
        save_url(message.text)

def dispatch_unknown_user(message):
    voice_note = open("src/resources/voice/notacapuyo.ogg", "rb")
    bot.reply_to(message, f"Lo siento, {message.from_user.first_name} {message.from_user.last_name} no tienes permisos para usar este bot ⚡")
    bot.send_voice(message.chat.id, voice_note)