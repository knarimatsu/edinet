import boto3
import os
from datetime import datetime
import pytz
from dotenv import load_dotenv


load_dotenv()
dynamodb_client = boto3.client(
    "dynamodb",
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
    region_name=os.environ["REGION"],
)
table_name = os.environ["DYNAMODB_TABLE"]


def dynamodb_put(data):
    now = int(datetime.now(pytz.timezone("Asia/Tokyo")).timestamp() * 1000)
    response = dynamodb_client.put_item(
        TableName=table_name,
        Item={
            "secCode": {"S": str(data["secCode"])},
            "docID": {"S": str(data["docID"])},
            "created_at": {"S": str(now)},
            "name": {"S": data["name"]},
            "plResult": {
                "M": {
                    "netSales": {"S": data["plResult"]["netSales"]},
                    "operatingRevenue1": {"S": data["plResult"]["operatingRevenue1"]},
                    "grossProfit": {"S": data["plResult"]["grossProfit"]},
                    "operatingIncome": {"S": data["plResult"]["operatingIncome"]},
                    "ordinaryIncome": {"S": data["plResult"]["ordinaryIncome"]},
                    "incomeBeforeIncomeTaxes": {
                        "S": data["plResult"]["incomeBeforeIncomeTaxes"]
                    },
                    "profitLoss": {"S": data["plResult"]["profitLoss"]},
                }
            },
            "bsResult": {
                "M": {
                    "currentAssets": {"S": (data["bsResult"]["currentAssets"])},
                    "cash": {"S": (data["bsResult"]["cash"])},
                    "accountsReceivable": {
                        "S": (data["bsResult"]["accountsReceivable"])
                    },
                    "investmentSecurities": {
                        "S": (data["bsResult"]["investmentSecurities"])
                    },
                    "assets": {"S": (data["bsResult"]["assets"])},
                    "netAssets": {"S": (data["bsResult"]["netAssets"])},
                    "liabilities": {"S": (data["bsResult"]["liabilities"])},
                }
            },
            "cashFlowResult": {
                "M": {
                    "depreciationAndAmortization": {
                        "S": data["cashFlowResult"]["depreciationAndAmortization"]
                    },
                    "impairmentLoss": {"S": data["cashFlowResult"]["impairmentLoss"]},
                    "operatingActivities": {
                        "S": data["cashFlowResult"]["operatingActivities"]
                    },
                    "investmentActivities": {
                        "S": data["cashFlowResult"]["investmentActivities"]
                    },
                    "financingActivities": {
                        "S": data["cashFlowResult"]["financingActivities"]
                    },
                    "dividendsPaid": {"S": data["cashFlowResult"]["dividendsPaid"]},
                }
            },
        },
    )
    return response


def get(code):
    response = dynamodb_client.get_item(TableName=table_name, Key=code)
    return response
