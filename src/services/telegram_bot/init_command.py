from services import telegram_bot

bot = telegram_bot.get_instance()
@bot.message_handler(commands=['start', 'help', 'ayuda'])
def cmd_start(message):
    bot.reply_to(message, "Aloha, en que te puedo ayudar? ⚡")