# Load .env
from dotenv import load_dotenv
from os import getenv
import requests


def find_database_pages():
    database = getenv("NOTION_DATABASE_ID")
    url = f"https://api.notion.com/v1/databases/{ database }/query"
    headers = {
        "Authorization": "Bearer " + getenv("NOTION_INTEGRATION_TOKEN"),
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    payload = {
        "page_size": 100
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()
    print(data)