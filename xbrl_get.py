# XBRLファイルをダウンロードし、解凍するスクリプト
import requests
import os
from dotenv import load_dotenv
import zipfile

load_dotenv()


def download_xbrl_file(doc_id: str):
    api_key = os.environ["API_KEY"]
    url = "https://api.edinet-fsa.go.jp/api/v2/documents/" + doc_id

    params = {"type": 1, "Subscription-Key": api_key}

    response = requests.get(url, params=params)

    # XBRLファイルをダウンロード
    if response.status_code == 200:
        with open("XBRL_" + doc_id + ".zip", "wb") as file:
            file.write(response.content)
        print("ファイルが正常にダウンロードされました")
    else:
        print(
            "ファイルのダウンロードに失敗しました\nステータスコード:{}".format(
                response.status_code
            )
        )

    # zipファイルを解凍
    with zipfile.ZipFile("XBRL_" + doc_id + ".zip", "r") as zip_ref:
        zip_ref.extractall(".")
    print("ファイルが正常に解凍されました")

    os.remove("XBRL_" + doc_id + ".zip")
    print("XBRLのzipファイルを削除しました")

    os.rename("XBRL", "XBRL_" + doc_id)
    print("フォルダ名が正常に変更されました")
