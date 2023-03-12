from dotenv import load_dotenv
from os import getenv
import requests

def set_item_categories(item, categories):
    print("--------------------")
    print(categories)
    headers = {
        "Authorization": "Bearer " + getenv("NOTION_INTEGRATION_TOKEN"),
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    page_id = item.get("id")
    page_url = f"https://api.notion.com/v1/pages/{ page_id }"
    payload = {
        "properties": {
            "Categories": {
                "multi_select": categories
            }
        }
    }

    response = requests.patch(page_url, json=payload, headers=headers)
    print(response.json())
    return response.json()
    

