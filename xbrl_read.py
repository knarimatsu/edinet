# XBRLファイルを読み込んで、必要なデータを取得するスクリプト
import os
from lxml import etree
from bs4 import BeautifulSoup

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


def get_xbrl_data(doc_id, sec_code, filter_name):
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
    # 売上
    revenues = soup.find("jppfs_cor:NetSales", contextRef="CurrentYearDuration")
    if revenues is None:
        revenues = soup.find(
            "jppfs_cor:NetSales", contextRef="CurrentYearDuration_NonConsolidatedMember"
        )
    if revenues is not None:
        data["plResult"]["netSales"] = revenues.text

    # 営業収益
    operating_revenue = soup.find(
        "jppfs_cor:OperatingRevenue1", contextRef="CurrentYearDuration"
    )
    if operating_revenue is None:
        operating_revenue = soup.find(
            "jppfs_cor:OperatingRevenue1",
            contextRef="CurrentYearDuration_NonConsolidatedMember",
        )
    if operating_revenue is not None:
        data["plResult"]["operatingRevenue1"] = operating_revenue.text

    # 売上総利益
    gross_profit = soup.find("jppfs_cor:GrossProfit", contextRef="CurrentYearDuration")
    if gross_profit is None:
        gross_profit = soup.find(
            "jppfs_cor:GrossProfit",
            contextRef="CurrentYearDuration_NonConsolidatedMember",
        )
    if gross_profit is not None:
        data["plResult"]["grossProfit"] = gross_profit.text

    # 営業利益
    operating_income = soup.find(
        "jppfs_cor:OperatingIncome", contextRef="CurrentYearDuration"
    )
    if operating_income is None:
        operating_income = soup.find(
            "jppfs_cor:OperatingIncome",
            contextRef="CurrentYearDuration_NonConsolidatedMember",
        )
    if operating_income is not None:
        data["plResult"]["operatingIncome"] = operating_income.text

    # 経常利益
    ordinary_income = soup.find(
        "jppfs_cor:OrdinaryIncome", contextRef="CurrentYearDuration"
    )
    if ordinary_income is None:
        ordinary_income = soup.find(
            "jppfs_cor:OrdinaryIncome",
            contextRef="CurrentYearDuration_NonConsolidatedMember",
        )
    if ordinary_income is not None:
        data["plResult"]["ordinaryIncome"] = ordinary_income.text

    # 税引き前当期純利益
    income_before_tax = soup.find(
        "jppfs_cor:IncomeBeforeIncomeTaxes", contextRef="CurrentYearDuration"
    )
    if income_before_tax is None:
        income_before_tax = soup.find(
            "jppfs_cor:IncomeBeforeIncomeTaxes",
            contextRef="CurrentYearDuration_NonConsolidatedMember",
        )
    if income_before_tax is not None:
        data["plResult"]["incomeBeforeIncomeTaxes"] = income_before_tax.text

    # 当期純利益
    profit_loss = soup.find("jppfs_cor:ProfitLoss", contextRef="CurrentYearDuration")
    if profit_loss is None:
        profit_loss = soup.find(
            "jppfs_cor:ProfitLoss",
            contextRef="CurrentYearDuration_NonConsolidatedMember",
        )
    if profit_loss is not None:
        data["plResult"]["profitLoss"] = profit_loss.text

    # 減価償却費
    depreciation = soup.find(
        "jppfs_cor:DepreciationAndAmortizationOpeCF", contextRef="CurrentYearDuration"
    )
    if depreciation is None:
        depreciation = soup.find(
            "jppfs_cor:DepreciationAndAmortizationOpeCF",
            contextRef="CurrentYearDuration_NonConsolidatedMember",
        )
    if depreciation is not None:
        data["cashFlowResult"]["depreciationAndAmortization"] = depreciation.text

    # 減損損失
    impairment_loss = soup.find(
        "jppfs_cor:ImpairmentLossOpeCF",
        contextRef="CurrentYearDuration",
    )
    if impairment_loss is None:
        impairment_loss = soup.find(
            "jppfs_cor:ImpairmentLossOpeCF",
            contextRef="CurrentYearDuration_NonConsolidatedMember",
        )
    if impairment_loss is not None:
        data["cashFlowResult"]["impairmentLoss"] = impairment_loss.text

    # 営業活動によるキャッシュフロー
    operating_cash_flow = soup.find(
        "jppfs_cor:NetCashProvidedByUsedInOperatingActivities",
        contextRef="CurrentYearDuration",
    )
    if operating_cash_flow is None:
        operating_cash_flow = soup.find(
            "jppfs_cor:NetCashProvidedByUsedInOperatingActivities",
            contextRef="CurrentYearDuration_NonConsolidatedMember",
        )
    if operating_cash_flow is not None:
        data["cashFlowResult"]["operatingActivities"] = operating_cash_flow.text

    # 投資活動によるキャッシュフロー
    investment_cash_flow = soup.find(
        "jppfs_cor:NetCashProvidedByUsedInInvestmentActivities",
        contextRef="CurrentYearDuration",
    )
    if investment_cash_flow is None:
        investment_cash_flow = soup.find(
            "jppfs_cor:NetCashProvidedByUsedInInvestmentActivities",
            contextRef="CurrentYearDuration_NonConsolidatedMember",
        )
    if investment_cash_flow is not None:
        data["cashFlowResult"]["investmentActivities"] = investment_cash_flow.text

    # 財務活動によるキャッシュフロー
    financing_cash_flow = soup.find(
        "jppfs_cor:NetCashProvidedByUsedInFinancingActivities",
        contextRef="CurrentYearDuration",
    )
    if financing_cash_flow is None:
        financing_cash_flow = soup.find(
            "jppfs_cor:NetCashProvidedByUsedInFinancingActivities",
            contextRef="CurrentYearDuration_NonConsolidatedMember",
        )
    if financing_cash_flow is not None:
        data["cashFlowResult"]["financingActivities"] = financing_cash_flow.text

    # 配当金の支払い
    dividend_payment = soup.find(
        "jppfs_cor:CashDividendsPaidFinCF", contextRef="CurrentYearDuration"
    )
    if dividend_payment is None:
        dividend_payment = soup.find(
            "jppfs_cor:CashDividendsPaidFinCF",
            contextRef="CurrentYearDuration_NonConsolidatedMember",
        )
    if dividend_payment is not None:
        data["cashFlowResult"]["dividendsPaid"] = dividend_payment.text

    # 流動資産
    current_assets = soup.find(
        "jppfs_cor:CurrentAssets", contextRef="CurrentYearInstant"
    )
    if current_assets is None:
        current_assets = soup.find(
            "jppfs_cor:CurrentAssets",
            contextRef="CurrentYearInstant_NonConsolidatedMember",
        )
    if current_assets is not None:
        data["bsResult"]["currentAssets"] = current_assets.text

    # 現金及び預金
    cash_and_deposit = soup.find(
        "jppfs_cor:CashAndCashEquivalents", contextRef="CurrentYearInstant"
    )
    if cash_and_deposit is None:
        cash_and_deposit = soup.find(
            "jppfs_cor:CashAndCashEquivalents",
            contextRef="CurrentYearInstant_NonConsolidatedMember",
        )
    if cash_and_deposit is not None:
        data["bsResult"]["cash"] = cash_and_deposit.text

    # 売掛金
    accounts_receivable = soup.find(
        "jppfs_cor:AccountsReceivableTrade", contextRef="CurrentYearInstant"
    )
    if accounts_receivable is None:
        accounts_receivable = soup.find(
            "jppfs_cor:AccountsReceivableTrade",
            contextRef="CurrentYearInstant_NonConsolidatedMember",
        )
    if accounts_receivable is not None:
        data["bsResult"]["accountsReceivable"] = accounts_receivable.text

    # 投資有価証券
    investment_securities = soup.find(
        "jppfs_cor:InvestmentSecurities", contextRef="CurrentYearInstant"
    )
    if investment_securities is None:
        investment_securities = soup.find(
            "jppfs_cor:InvestmentSecurities",
            contextRef="CurrentYearInstant_NonConsolidatedMember",
        )
    if investment_securities is not None:
        data["bsResult"]["investmentSecurities"] = investment_securities.text

    # 資産
    assets = soup.find("jppfs_cor:Assets", contextRef="CurrentYearInstant")
    if assets is None:
        assets = soup.find(
            "jppfs_cor:Assets",
            contextRef="CurrentYearInstant_NonConsolidatedMember",
        )
    if assets is not None:
        data["bsResult"]["assets"] = assets.text

    # 純資産
    net_assets = soup.find("jppfs_cor:NetAssets", contextRef="CurrentYearInstant")
    if net_assets is None:
        net_assets = soup.find(
            "jppfs_cor:NetAssets",
            contextRef="CurrentYearInstant_NonConsolidatedMember",
        )
    if net_assets is not None:
        data["bsResult"]["netAssets"] = net_assets.text

    # 負債
    liabilities = soup.find("jppfs_cor:Liabilities", contextRef="CurrentYearInstant")
    if liabilities is None:
        liabilities = soup.find(
            "jppfs_cor:Liabilities",
            contextRef="CurrentYearInstant_NonConsolidatedMember",
        )
    if liabilities is not None:
        data["bsResult"]["liabilities"] = liabilities.text
    return data
