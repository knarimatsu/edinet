import json
from time import sleep
from get_docid import get_id_list
from time import sleep
from xbrl_get import (
    download_xbrl_file,
    unzip_file,
    delete_zip_file,
    rename_file,
    delete_xbrl_dir,
)
from xbrl_read import get_xbrl_data
from xbrl_s3 import detect_xbrl_from_s3, get_xbrl_data_from_s3, upload_to_s3
from dynamodb import dynamodb_put


def lambda_handler(event, context):

    docment_id_list = get_id_list()
    if docment_id_list is None:
        return {"statusCode": 200, "body": "No data"}

    for doc_id in docment_id_list:
        download_xbrl_file(doc_id["docID"])
        unzip_file(doc_id["docID"])
        rename_file(doc_id["docID"])
        delete_zip_file(doc_id["docID"])
        upload_to_s3(doc_id["docID"])
        delete_xbrl_dir(doc_id["docID"])

    for docment in docment_id_list:
        # data = get_xbrl_data(docment["docID"], docment["secCode"], docment["name"])
        object_path = detect_xbrl_from_s3(docment["docID"])
        print(object_path)
        data = get_xbrl_data_from_s3(
            object_path, docment["secCode"], docment["docID"], docment["name"]
        )
        print(json.dumps(data, indent=4, ensure_ascii=False))
        # ここにAPIを叩く処理を書く
        put_response = dynamodb_put(data)
        print(put_response)

    return {
        "statusCode": 200,
        "body": json.dumps(docment_id_list, indent=4, ensure_ascii=False),
    }
