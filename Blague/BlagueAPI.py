import os
import requests
import json
from time import sleep

from dotenv import load_dotenv


def blague_api():
    load_dotenv()

    url = "https://www.blagues-api.fr/api/random?disallow=dark&disallow=limit"

    headers = {
        'Authorization': f"Bearer {os.getenv('BLAGUE_API')}"
    }

    response = requests.request("GET", url, headers=headers, data={})
    response_json = json.loads(response.text)
    blague = response_json['joke']
    reponse = response_json['answer']

    list_message = [blague, reponse]
    return list_message

#print(blague_api())
