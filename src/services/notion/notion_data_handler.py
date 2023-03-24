
from services.notion.find_database_categories import find_database_categories


class notion_data_handler:
    # Singleton to handle the categories data
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if notion_data_handler.__instance == None:
            notion_data_handler()
        return notion_data_handler.__instance
    
    def __init__(self):
        """ Virtually private constructor. """
        if notion_data_handler.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            notion_data_handler.__instance = self
            self.categories = find_database_categories()
            self.selected_categories = {}
            self.created_item = None

    def add_category(self, category):
        self.categories.append(category)

    def add_selected_category(self, category):
        self.selected_categories[category] = True

    def get_categories(self):
        return self.categories
    
    def get_selected_categories(self):

        return self.selected_categories
    
    def clear_categories(self):
        self.categories.clear()
        self.categories = find_database_categories()

    def clear_selected_categories(self):
        self.selected_categories.clear()

    def add_multiple_categories(self, categories):
        for category in categories:
            self.add_category(category)

    def add_multiple_selected_categories(self, categories):
        for category in categories:
            if category not in self.categories:
                self.add_category(category)
    
    def set_created_item(self, item):
        self.created_item = item

    def get_created_item(self):
        return self.created_item
    
    def clear_created_item(self):
        self.created_item = None