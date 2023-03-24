from os import getenv
from dotenv import load_dotenv
import requests
import json
load_dotenv()

def save_url(data):
    print("Saving url: " + data.text)
    endpoint = "https://api.notion.com/v1/pages"
    # database_id = getenv("NOTION_DATABASE_ID") 
    # set database id if data.from_user.username == "rcanelav" use NOTION_DATABASE_ID if "AnitaPunetes" use ANTIA_DB"
    database_id = getenv("NOTION_DATABASE_ID") if data.from_user.username == "rcanelav" else getenv("ANTIA_DB")
    api_key = getenv("NOTION_INTEGRATION_TOKEN") if data.from_user.username == "rcanelav" else getenv("ANTIA_INTEGRATION_TOKEN")
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
            "url": data.text
        },
        "Categories": {
            "type": "multi_select",
            "multi_select": [
                
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

    # print(response.json().get("id"))
    return response.json()