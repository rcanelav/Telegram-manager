from dotenv import load_dotenv
from os import getenv
import threading
import telebot
from services.notion.find_database_categories import find_database_categories
from services.notion.save_new_url import save_url
from services.notion.set_item_categories import set_item_categories
from utils.white_list import white_list
import requests
load_dotenv()

bot_token = getenv("BOT_TOKEN")
bot = telebot.TeleBot(bot_token)
categories = None
selected_categories = {}

@bot.message_handler(commands=['start', 'help', 'ayuda'])
def cmd_start(message):
    bot.reply_to(message, "Aloha, en que te puedo ayudar? ⚡")

@bot.message_handler(content_types=['text'])
def bot_mensajes_texto(message):
    # If the user is not in the white list, dispatch unknown user and return
    if message.from_user.username not in white_list().get_users():
        dispatch_unknown_user(message)
        return

    # If the message is a url, extract the title
    if "https://" in message.text:
        # get the title from the previsually extracted url  save in in the global variable created_item
        global created_item
        global categories
        categories = find_database_categories(message)
        created_item = save_url(message)
     
        markup = telebot.types.InlineKeyboardMarkup(row_width=1)
        for option in categories:
            markup.add(telebot.types.InlineKeyboardButton(option["name"], callback_data=option["name"]))
        markup.add(telebot.types.InlineKeyboardButton("Cancelar", callback_data="Cancelar"))
        markup.add(telebot.types.InlineKeyboardButton("Agregar otras", callback_data="Agregar"))
        confirm_button = telebot.types.InlineKeyboardButton("Confirmar", callback_data="Confirmar")
        # change confirm button color
        confirm_button.color = "primary"
        markup.add(confirm_button)
        bot.send_message(message.chat.id, "Seleccione una o varias categorías:", reply_markup=markup)

# if call.data in categories name
@bot.callback_query_handler(func=lambda call: call.data in  [category["name"] for category in categories] or call.data in ["Cancelar", "Confirmar", "Agregar"])
def process_callback(call):
    # add the category to the list
    if call.data not in ["Cancelar", "Confirmar", "Agregar"]:
        selected_categories[call.data] = True

    elif call.data == "Cancelar":
        bot.send_message(call.message.chat.id, "Cancelando")
        # Hide inline buttons
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == "Confirmar":
        bot.send_message(call.message.chat.id, "Confirmado")
        # Hide inline buttons
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        # Append the id of the category to the categories that match the name
        # Create a structure like this:
        # {
        #     "name": "category_name",
        #     "id": "category_id"
        # }
        # selected_categories = [{"name": "category_name", "id": "category_id"}]

        data_structure = []
        for selected_category in selected_categories:
            if selected_category in [category["name"] for category in categories]:
                for category in categories:
                    if category["name"] == selected_category:
                        data_structure.append(category)
            # If the category is not in the database, add it
            else:
                new_category = {"name": selected_category}
                categories.append(new_category)
                data_structure.append(new_category)
        username = call.message.from_user.username
        set_item_categories(created_item, data_structure, username)
    elif call.data.lower() == "agregar":
        print("call.data: ", call.data)

        bot.send_message(call.message.chat.id, "Escriba las categorías que desea agregar separadas por comas ❗")
        bot.register_next_step_handler(call.message, add_categories)

def add_categories(message):
    categories_to_add = message.text.split(",")

    for category in categories_to_add:
        category = category.strip()
        if category not in [category["name"] for category in categories]:
            categories.append({"name": category})
            selected_categories[category] = True
        else:
            selected_categories[category] = True

# Start the bot
def start_bot():
    bot.infinity_polling()

# Sends a voice note to the user and replies to the message
def dispatch_unknown_user(message):
    voice_note = open("src/resources/voice/notacapuyo.ogg", "rb")
    bot.reply_to(message, f"Lo siento, {message.from_user.first_name} {message.from_user.last_name} no tienes permisos para usar este bot ⚡")
    bot.send_voice(message.chat.id, voice_note)

if __name__ == '__main__':
    # find_database_pages()
    # print("Bot started")
    # bot_listener = threading.Thread(name="bot_rayci", target=start_bot)
    # bot_listener.start()
    start_bot()
    # find_database_categories();




