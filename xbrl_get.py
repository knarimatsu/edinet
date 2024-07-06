# XBRLファイルをダウンロードし、解凍するスクリプト
import requests
import os
from dotenv import load_dotenv
import zipfile
import boto3

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

    # zipファイルを削除
    os.remove("XBRL_" + doc_id + ".zip")
    print("XBRLのzipファイルを削除しました")

    # フォルダ名を変更
    os.rename("XBRL", "XBRL_" + doc_id)
    print("フォルダ名が正常に変更されました")

    # S3にアップロード
    s3 = boto3.client("s3")
    bucket_name = os.environ["BUCKET_NAME"]
    # 変更したフォルダをS3にアップロード


download_xbrl_file("S100TYEA")
