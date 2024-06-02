import requests
import datetime
import json
date = datetime.date.today()

api_key = 'c26a08a3c4b74f3a984699735c5f077f'
url = 'https://api.edinet-fsa.go.jp/api/v2/documents.json'

params = {
    'date': str(date),
    'type':2,
    'Subscription-Key': api_key,
}

response = requests.get(url=url, params=params)
response_body = json.loads(response.text)

print(response_body['results'])
# print(type(response_body))