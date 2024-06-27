# XBRLファイルを読み込んで、必要なデータを取得するスクリプト
import os
from lxml import etree
from bs4 import BeautifulSoup
from xbrl_content_list import xbrl_content_list

xbrl_file_path = ""


def detect_xbrl(dir_name):
    os.chdir("XBRL_" + dir_name)
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


def find_data(soup, tag_name, context_ref, context_ref_nonconsolidatedMember):
    """_summary_

    Returns:
        _type_: _description_
    """

    result = soup.find(tag_name, contextRef=context_ref)
    if result is None:
        result = soup.find(tag_name, contextRef=context_ref_nonconsolidatedMember)
    if result is not None:
        return result.text
    else:
        return ""


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
    data = {
        "secCode": sec_code,
        "docID": doc_id,
        "name": filter_name,
        "plResult": {
            "netSales": "",
            "operatingRevenue1": "",
            "grossProfit": "",
            "operatingIncome": "",
            "ordinaryIncome": "",
            "incomeBeforeIncomeTaxes": "",
            "profitLoss": "",
        },
        "bsResult": {
            "currentAssets": "",
            "cash": "",
            "accountsReceivable": "",
            "investmentSecurities": "",
            "assets": "",
            "netAssets": "",
            "liabilities": "",
        },
        "cashFlowResult": {
            "depreciationAndAmortization": "",
            "impairmentLoss": "",
            "operatingActivities": "",
            "investmentActivities": "",
            "financingActivities": "",
            "dividendsPaid": "",
        },
    }

    for item in xbrl_content_list:
        data[item["statement_type"]][item["item"]] = find_data(
            soup,
            item["tag"],
            item["context_ref"],
            item["context_ref_nonconsolidatedMember"],
        )
    return data
