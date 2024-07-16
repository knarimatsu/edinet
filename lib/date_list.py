from pandas import pandas as pd
from datetime import datetime, timedelta


def get_date_range(start_date, end_date):
    # 日付の範囲を生成
    date_range = pd.date_range(start=start_date, end=end_date)
    # 日付のリストを生成
    date_list = date_range.strftime("%Y-%m-%d").tolist()
    return date_list


# 例
start_date = "2013-01-01"
a_year_end_date = (
    datetime.strptime(start_date, "%Y-%m-%d")
    + timedelta(days=(365 if isLeapYear(int(start_date[:4])) else 364))
).strftime("%Y-%m-%d")

isLeapYear = lambda x: x % 4 == 0 and (x % 100 != 0 or x % 400 == 0)
dates = get_date_range(start_date, a_year_end_date)
print(dates)
