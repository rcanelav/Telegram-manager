from services.notion.notion_data_handler import notion_data_handler
from services.notion.set_item_categories import set_item_categories
from services.telegram_bot.telegram_bot import telegram_bot


bot = telegram_bot.get_instance().bot
@bot.callback_query_handler(func=lambda call: call.data is not None)
def process_callback(call):
    print(call.data)
    selected_categories = notion_data_handler.get_selected_categories()
    # add the category to the list
    if call.data not in ["Cancelar", "Confirmar", "Agregar"]:
        notion_data_handler.add_selected_category(call.data)

    elif call.data == "Cancelar":
        bot.send_message(call.message.chat.id, "Cancelando")
        # Hide inline buttons
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == "Confirmar":
        print("ME CAGOOOOOOO")
        bot.send_message(call.message.chat.id, "puta")
        # Hide inline buttons
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        # Append the id of the category to the categories that match the name
        # Create a structure like this:
        # {
        #     "name": "category_name",
        #     "id": "category_id"
        # }
        # selected_categories = [{"name": "category_name", "id": "category_id"}]
        categories = notion_data_handler.get_categories()
        
        # data_structure = []
        for selected_category in selected_categories:
            if selected_category in [category["name"] for category in categories]:
                for category in categories:
                    if category["name"] == selected_category:
                        # data_structure.append(category)
                        notion_data_handler.add_selected_category(category)
            # If the category is not in the database, add it
            else:
                new_category = {"name": selected_category}
                categories.append(new_category)
                # data_structure.append(new_category)
                notion_data_handler.add_selected_category(new_category)

        print("-----------------")
        print(notion_data_handler.get_selected_categories())
        set_item_categories(notion_data_handler.get_created_item, selected_categories)
        notion_data_handler.clear_categories()
        notion_data_handler.clear_selected_categories()

    elif call.data.lower() == "agregar":
        print("call.data: ", call.data)

        bot.send_message(call.message.chat.id, "Escriba las categorías que desea agregar separadas por comas ❗")
        bot.register_next_step_handler(call.message, add_categories)

def add_categories(message):
    categories_to_add = message.text.split(",")

    for category in categories_to_add:
        category = category.strip()
        if category not in [category["name"] for category in categories]:
            notion_data_handler.add_category(category)
        
        notion_data_handler.add_selected_category(category)