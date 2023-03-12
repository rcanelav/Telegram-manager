from dotenv import load_dotenv
from os import getenv
load_dotenv()

class white_list:
    def __init__(self):
        self.users = []
        DEFAULT_USERS = getenv("DEFAULT_USERS")
        # DEFAULT_USERS is a string containing a list of usernames separated by commas
        # example ["user1", "user2", "user3"]
        # transform it into an array
        DEFAULT_USERS = DEFAULT_USERS.split(",")
        for user in DEFAULT_USERS:
            # Remove the spaces and all the characters that are not letters or numbers
            parsed_user = user.strip().replace(" ", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("'", "").replace('"', "")
            print(parsed_user)
            self.users.append(parsed_user)

    def add_user(self, username):
        if username not in self.users:
            self.users.append(username)

    def remove_user(self, username):
        if username in self.users:
            self.users.remove(username)

    def update_user(self, old_username, new_username):
        if old_username in self.users:
            self.users.remove(old_username)
            self.users.append(new_username)

    def get_users(self):
        return self.users