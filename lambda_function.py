import json
from time import sleep
from get_docid import get_id_list

def lambda_handler(event, context):
    
    print("昨日発行された一般企業の有価証券報告書のIDを取得します")
    docment_id_list = get_id_list()
    print(docment_id_list)
    sleep(5)
    print("---------------------------")
    print("取得完了しました")
    print("---------------------------")
    
    return {
        'statusCode': 200,
        'body': docment_id_list
    }