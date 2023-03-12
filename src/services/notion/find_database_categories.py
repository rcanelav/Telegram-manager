from dotenv import load_dotenv
from os import getenv
import requests

def find_database_categories():
    database = getenv("NOTION_DATABASE_ID")
    url = f"https://api.notion.com/v1/databases/{ database }"
    headers = {
        "Authorization": "Bearer " + getenv("NOTION_INTEGRATION_TOKEN"),
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    # Retrieve all the categories from the database
   

    response = requests.get(url, headers=headers)

    data = response.json()
    # print(data)
    # Create an set of categories to avoid duplicates
    categories = []
    for category in data.get("properties").get("Categories").get("multi_select").get("options"):
        if category not in categories:
            categories.append(category)


    # print(categories)
    return categories


