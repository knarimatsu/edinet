import os
from time import sleep
from get_docid import get_id_list
from xbrl_get import download_xbrl_file
from xbrl_read import detect_xbrl, get_xbrl_data


# ['S100TLCL', 'S100TLBC']

print("昨日発行された一般企業の有価証券報告書のIDを取得します")
docment_id_list = get_id_list()
print(docment_id_list)
print("---------------------------")
print("取得完了しました")
print("---------------------------")

print("取得したIDからの有価証券報告書をダウンロードします")
for doc_id in docment_id_list:
    download_xbrl_file(doc_id)
    sleep(2)
print("---------------------------")
print("すべてのダウンロード完了しました")
print("---------------------------")

for doc_id in docment_id_list:
    print("---------------------------")
    get_xbrl_data(doc_id)
    os.chdir("..")
    os.chdir("..")

print("---------------------------")
