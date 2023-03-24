from dotenv import load_dotenv
from os import getenv
import requests
load_dotenv()

def set_item_categories(item, categories, username):
    api_key = getenv("NOTION_INTEGRATION_TOKEN") if username == "rcanelav" else getenv("ANTIA_INTEGRATION_TOKEN")

    headers = {
        "Authorization": "Bearer " + api_key,
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
    # print(response.json())
    return response.json()
    

