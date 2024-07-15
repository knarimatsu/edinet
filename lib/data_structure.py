def data_structure(sec_code, doc_id, filter_name):
    return {
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
