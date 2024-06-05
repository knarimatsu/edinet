import requests
import os
from dotenv import load_dotenv
import zipfile

load_dotenv()

doc_id = input("ファイル名:")
api_key = os.environ["API_KEY"]
url = "https://api.edinet-fsa.go.jp/api/v2/documents/{}?Subscription-Key={}&type=5".format(
    doc_id, api_key
)

response = requests.get(url)

if response.status_code == 200:
    with open("{}.zip".format(doc_id), "wb") as file:
        file.write(response.content)
    print("ファイルが正常にダウンロードされました")
else:
    print(
        "ファイルのダウンロードに失敗しました\nステータスコード:{}".format(
            response.status_code
        )
    )

with zipfile.ZipFile("{}.zip".format(doc_id), "r") as zip_ref:
    zip_ref.extractall(".")
print("ファイルが正常に解凍されました")

os.remove("{}.zip".format(doc_id))
print("zipファイルを削除しました")

os.rename("XBRL_TO_CSV", doc_id)
print("フォルダ名が正常に変更されました")
