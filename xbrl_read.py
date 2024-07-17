# XBRLファイルを読み込んで、必要なデータを取得するスクリプト
import os
from bs4 import BeautifulSoup
from lib.xbrl_content_list import xbrl_content_list
import boto3
import re
from dotenv import load_dotenv
import json
from lib.find_data import find_data
from lib.data_structure import data_structure


load_dotenv()
xbrl_file_path = ""
s3_client = boto3.client(
    "s3",
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
)


def detect_xbrl(doc_id):
    os.chdir("XBRL_" + doc_id)
    os.chdir("PublicDoc")
    file_name = None
    for file in os.listdir():
        if file.endswith(".xbrl"):
            file_name = file
            break

    if file_name is None:
        print("No matching XBRL file found.")
        exit()

    return file_name


def get_xbrl_data(doc_id, sec_code, filter_name):
    """_summary_

    Args:
        doc_id (_type_): _description_
        sec_code (_type_): _description_
        filter_name (_type_): _description_

    Returns:
        _type_: _description_
    """

    target_xbrl_file = detect_xbrl(doc_id)

    with open(target_xbrl_file, "r", encoding="utf-8") as file:
        xbrl_content = file.read()

    os.chdir("..")
    os.chdir("..")

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
