from dotenv import load_dotenv
from os import getenv
import requests
load_dotenv()

def find_database_categories(data):
    database = getenv("NOTION_DATABASE_ID") if data.from_user.username == "rcanelav" else getenv("ANTIA_DB")
    api_key = getenv("NOTION_INTEGRATION_TOKEN") if data.from_user.username == "rcanelav" else getenv("ANTIA_INTEGRATION_TOKEN")
    url = f"https://api.notion.com/v1/databases/{ database }"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    # Retrieve all the categories from the database
    response = requests.get(url, headers=headers)

    data = response.json()
    # Create an set of categories to avoid duplicates
    categories = []
    for category in data.get("properties").get("Categories").get("multi_select").get("options"):
        if category not in categories:
            categories.append(category)

    return categories


