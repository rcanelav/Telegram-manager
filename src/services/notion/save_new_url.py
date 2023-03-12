from os import getenv
from dotenv import load_dotenv
import requests
import json
load_dotenv()

def save_url(url):
    print("Saving url: " + url)
    endpoint = "https://api.notion.com/v1/pages"
    database_id = getenv("NOTION_DATABASE_ID")
    api_key = getenv("NOTION_INTEGRATION_TOKEN")
    headers = {
        "Notion-Version": "2021-05-13",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # ROW FORMAT   TITLE <STING> | URL <URL> | CATEGORIES <MULTI_SELECT>
    # Insert the title and url
    properties = {
        "Title": {
            "type": "title",
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": "Test"
                    }
                }
            ]
        },
        "URL": {
            "type": "url",
            "url": url
        },
        "Categories": {
            "type": "multi_select",
            "multi_select": [
                {
                    "name": "Python"
                }
            ]
        }
    }

    # Create the payload for the API request
    payload = {
        "parent": {"database_id": database_id},
        "properties": properties
    }

    # Convert the payload to a JSON string
    payload_str = json.dumps(payload)

    # Make the API request
    response = requests.post(endpoint, headers=headers, data=payload_str)

    print(response.json().get("id"))
    return response.json()