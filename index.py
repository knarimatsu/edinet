import json
import aiohttp
import asyncio
from time import sleep
from get_docid import get_id_list
from xbrl_get import download_xbrl_file
from xbrl_read import detect_xbrl, get_xbrl_data
from dynamodb import dynamodb_put


# ['S100TLCL', 'S100TLBC']

print("昨日発行された一般企業の有価証券報告書のIDを取得します")
docment_id_list = get_id_list()
print(docment_id_list)
sleep(5)
print("---------------------------")
print("取得完了しました")
print("---------------------------")


print("取得したIDからの有価証券報告書をダウンロードします")
for doc_id in docment_id_list:
    download_xbrl_file(doc_id["docID"])
    sleep(2)
print("---------------------------")
print("すべてのダウンロード完了しました")
print("---------------------------")

for docment in docment_id_list:
    print("---------------------------")
    data = get_xbrl_data(docment["docID"], docment["secCode"], docment["name"])
    print(json.dumps(data, indent=4, ensure_ascii=False))
    # ここにAPIを叩く処理を書く
    put_response = dynamodb_put(data)
    print(put_response)
