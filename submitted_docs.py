import requests
import datetime
import json
import os
from dotenv import load_dotenv

load_dotenv()

date = datetime.date.today()

api_key = os.environ["API_KEY"]
url = "https://api.edinet-fsa.go.jp/api/v2/documents.json"

params = {
    "date": str(date),
    "type": 2,
    "Subscription-Key": api_key,
}

response = requests.get(url=url, params=params)
response_body = json.loads(response.text)

print(response_body["results"])
