import boto3
import json
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
from lib.xbrl_content_list import xbrl_content_list
from lib.find_data import find_data
from lib.data_structure import data_structure
import re

load_dotenv()


s3_client = boto3.client(
    "s3",
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
)
bucket_name = os.environ["BUCKET_NAME"]


def detect_xbrl_from_s3(doc_id):
    """S3から指定したドキュメントIDをもつXBRLファイルを検出する関数

    Args:
        doc_id (_type_): ドキュメントのID

    Returns:
        _type_: _description_
    """

    xbrl_pattern = re.compile(r".*\.xbrl")
    response = s3_client.list_objects_v2(
        Bucket=bucket_name, Prefix="XBRL_" + doc_id + "/PublicDoc/"
    )
    target_xbrl_file = [
        content["Key"]
        for content in response["Contents"]
        if xbrl_pattern.match(content["Key"])
    ][0]

    return target_xbrl_file


def get_xbrl_data_from_s3(object_path, sec_code, doc_id, filter_name):
    """S3からXBRLファイルを取得し、指定したデータを取得する関数

    Args:
        object_path (_type_): _description_
        sec_code (_type_): _description_
        doc_id (_type_): _description_
        filter_name (_type_): _description_

    Returns:
        _type_: _description_
    """
    response = s3_client.get_object(Bucket=bucket_name, Key=object_path)
    xbrl_content = response["Body"].read().decode("utf-8")
    soup = BeautifulSoup(xbrl_content, features="xml")
    data = data_structure(sec_code, doc_id, filter_name)

    for item in xbrl_content_list:
        data[item["statement_type"]][item["item"]] = find_data(
            soup,
            item["tag"],
            item["context_ref"],
            item["context_ref_nonconsolidatedMember"],
        )
    return data


def upload_to_s3(doc_id: str):
    """

    Args:
        doc_id (str): _description_
    """
    folder_name = "XBRL_" + doc_id
    for root, dirs, files in os.walk(folder_name):
        for file in files:
            try:
                file_path = os.path.join(root, file).replace("\\", "/")
                s3_client.upload_file(
                    file_path,
                    bucket_name,
                    file_path,
                )
            except FileNotFoundError:
                print("ファイルが見つかりません")

    print(doc_id + "のフォルダがS3にアップロードされました")
