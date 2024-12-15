import os
import re
import chardet
from dotenv import load_dotenv
from extraction_value import get_bs_value, get_pl_value


load_dotenv()


def read_csv(dir_name):
    os.chdir(dir_name)
    file_name = None
    for file in os.listdir():
        if file.startswith("jpcrp") and file.endswith(".csv"):
            file_name = file
            break

    if file_name is None:
        print("No matching CSV file found.")
        exit()

    with open(file_name, "rb") as file:
        data = file.read()
    result = chardet.detect(data)
    encoding = result["encoding"]
    with open(file_name, "r", encoding=encoding) as file:
        data = file.read()

    return data


csv_data = read_csv("S100TI8V")
balance_sheet = []
# # 資産
assets = get_bs_value(csv_data, "jppfs_cor:Assets.*")
balance_sheet.append({"assets": assets})
# 現金及び預金
cash = get_bs_value(csv_data, "jppfs_cor:CashAndDeposits.*")
balance_sheet.append({"cash": cash})
# 売掛金
accounts_receivable_trade = get_bs_value(
    csv_data, "jppfs_cor:AccountsReceivableTrade.*"
)
balance_sheet.append({"accounts_receivable_trade": accounts_receivable_trade})
# 流動資産
current_assets = get_bs_value(csv_data, "jppfs_cor:CurrentAssets.*")
balance_sheet.append({"current_assets": current_assets})
# 投資有価証券
investment_securities = get_bs_value(csv_data, "jppfs_cor:InvestmentSecurities.*")
balance_sheet.append({"investment_securities": investment_securities})
# 固定資産
non_current_assets = get_bs_value(csv_data, "jppfs_cor:NoncurrentAssets.*")
balance_sheet.append({"non_current_assets": non_current_assets})
# 負債
liabilities = get_bs_value(csv_data, "jppfs_cor:Liabilities.*")
balance_sheet.append({"liabilities": liabilities})
# 純資産
net_assets = get_bs_value(csv_data, "jppfs_cor:NetAssets.*")
balance_sheet.append({"net_assets": net_assets})
# 売上高
pe_statement = []
sales = get_pl_value(csv_data, "jppfs_cor:NetSales.*")
pe_statement.append({"sales": sales})
# 粗利益
gross_profit = get_pl_value(csv_data, "jppfs_cor:GrossProfit.*")
pe_statement.append({"gross_profit": gross_profit})
# 営業利益
operating_income = get_pl_value(csv_data, "jppfs_cor:OperatingIncome.*")
pe_statement.append({"operating_income": operating_income})
# 経常利益
ordinary_income = get_pl_value(csv_data, "jppfs_cor:OrdinaryIncome.*")
pe_statement.append({"ordinary_income": ordinary_income})
# 当期純利益
net_income = get_pl_value(csv_data, "jppfs_cor:ProfitLoss.*")
pe_statement.append({"net_income": net_income})
print("Balance Sheet")
for i in balance_sheet:
    print(i)
print("\n\n")
print("Profit and Loss Statement")
for i in pe_statement:
    print(i)
