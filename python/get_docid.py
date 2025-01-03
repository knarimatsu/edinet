# edinetのAPIを使用して、有価証券報告書のdocIDを取得するスクリプト

import requests
import os
from dotenv import load_dotenv
import datetime
import json
import re


load_dotenv()


def get_id_list(day):
    """その日にアップしたドキュメントの中から、
    有価証券報告書のdocIDを取得する関数

    Returns:
        _type_: 取得したIDを一覧で返す
    """

    pattern = re.compile(r"有価証券報告書*")
    api_key = os.environ["API_KEY"]
    url = "https://api.edinet-fsa.go.jp/api/v2/documents.json"
    yesterday = datetime.date.today() - datetime.timedelta(day)


    params = {"date": str(yesterday), "type": 2, "Subscription-Key": api_key}
    response = requests.get(url, params=params)
    json_data = json.loads(response.text)
    results = json_data["results"]

    data_list = list(
        filter(
            lambda x: x["fundCode"] is None
            and x["secCode"] is not None
            and pattern.match(x["docDescription"]),
            results,
        )
    )
    if len(data_list) == 0:
        print("データがありませんでした")
        return None

    docid_list = []
    for data in data_list:
        docid_list.append(
            {
                "docID": data["docID"],
                "secCode": data["secCode"],
                "name": data["filerName"],
            }
        )
    print(json.dumps(docid_list, indent=4, ensure_ascii=False))

    return docid_list
