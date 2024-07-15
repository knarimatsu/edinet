import json
from time import sleep
from get_docid import get_id_list
from xbrl_get import download_xbrl_file
from xbrl_read import get_xbrl_data
from dynamodb import dynamodb_put


# ['S100TLCL', 'S100TLBC']

print("昨日発行された一般企業の有価証券報告書のIDを取得します")
docment_id_list = get_id_list()
if docment_id_list is None:
    print("取得できるデータがありませんでした")
    exit()
print(docment_id_list)
print("---------------------------")
print("取得完了しました")
print("---------------------------")


print("取得したIDからの有価証券報告書をダウンロードします")
for doc_id in docment_id_list:
    download_xbrl_file(doc_id["docID"])
print("---------------------------")
print("すべてのダウンロード完了しました")
print("---------------------------")

for docment_id in docment_id_list:
    print("---------------------------")
    data = get_xbrl_data(docment_id["docID"], docment_id["secCode"], docment_id["name"])
    print(json.dumps(data, indent=4, ensure_ascii=False))
    # ここにAPIを叩く処理を書く
    put_response = dynamodb_put(data)
    print(put_response)
