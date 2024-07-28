# XBRLファイルをダウンロードし、解凍するスクリプト
import requests
import os
import shutil
from dotenv import load_dotenv
import zipfile
import boto3
import json

load_dotenv()


def download_xbrl_file(doc_id: str):
    """
    XBRLファイルをダウンロードし、解凍する関数
    Args:
        doc_id (str): 取得するべきXBRLファイルのdoc_id
    """
    api_key = os.environ["API_KEY"]
    url = "https://api.edinet-fsa.go.jp/api/v2/documents/" + doc_id

    params = {"type": 1, "Subscription-Key": api_key}

    response = requests.get(url, params=params)
    # print(json.dumps(response, indent=4, ensure_ascii=False))

    # XBRLファイルをダウンロード
    if response.status_code == 200:
        with open("/tmp/XBRL_" + doc_id + ".zip", "wb") as file:
            file.write(response.content)
        print(doc_id + "のファイルが正常にダウンロードされました")
        unzip_file(doc_id)
    else:
        print(
            "ファイルのダウンロードに失敗しました\nステータスコード:{}".format(
                response.status_code
            )
        )


def unzip_file(doc_id: str):
    """zipファイルを解凍する関数

    Args:
        doc_id (str): _description_
    """

    # zipファイルを解凍
    with zipfile.ZipFile("/tmp/XBRL_" + doc_id + ".zip", "r") as zip_ref:
        zip_ref.extractall(".")
    print(doc_id + "のファイルが正常に解凍されました")


def delete_zip_file(doc_id: str):
    # zipファイルを削除
    os.remove("/tmp/XBRL_" + doc_id + ".zip")
    print(doc_id + "のXBRLのzipファイルを削除しました")


def rename_file(doc_id: str):
    # フォルダ名を変更
    os.rename("XBRL", "/tmp/XBRL_" + doc_id)
    print(doc_id + "のフォルダ名が正常に変更されました")


def delete_xbrl_dir(doc_id: str):
    # "/tmp/XBRL_" + doc_idのついたディレクトリを削除
    xbrl_dir = "/tmp/XBRL_" + doc_id
    if os.path.exists(xbrl_dir):
        shutil.rmtree(xbrl_dir)
        print(doc_id + "のXBRLのディレクトリを削除しました")
    else:
        print("XBRLのディレクトリが見つかりません")
