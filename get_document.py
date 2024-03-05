import requests

domain = "https://disclosure.edinet-fsa.go.jp"
api = "/api"
version = "/v1"
detail = "/documents.json"
params = {"date": "2023-10-19", "type": "2"}

path = (
    domain
    + api
    + version
    + detail
    + "?date="
    + params["date"]
    + "&type="
    + params["type"]
)

res = requests.get(path)
print(res)
