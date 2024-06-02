# import zipfile
# import os
# import chardet
# from bs4 import BeautifulSoup

# zip_file_path = './xbrl/Xbrl_Search_20240521_111841.zip'
# exact_folder = './xbrl/extracted'

# with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#     zip_ref.extractall(exact_folder)

# for root, dirs, files in os.walk(exact_folder):
#     for file in files:
#         if file.endswith('.xbrl'):
#             xbrl_file_path = os.path.join(root, file)
#             break

# with open(xbrl_file_path, 'rb') as file:
#     raw_data = file.read()

# result = chardet.detect(raw_data)
# encoding = result['encoding']

# with open(xbrl_file_path, 'r', encoding=encoding) as file:
#     xbrl_content = file.read()

# soup = BeautifulSoup(xbrl_content, features='lxml')
# elements = soup.find_all('jpcrp_cor:OperatingRevenue')

# for element in elements:
#     print(element.text)

import zipfile
import os
from bs4 import BeautifulSoup
import chardet

# ZIPファイルのパス
zip_file_path = './xbrl/Xbrl_Search_20240521_111841.zip'
extract_folder = './xbrl/extracted'

# ZIPファイルを解凍
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

# 解凍されたファイルのパス（解凍されたフォルダの中のXBRLファイルを探す）
xbrl_file_path = None
for root, dirs, files in os.walk(extract_folder):
    for file in files:
        if file.endswith('.xbrl'):
            xbrl_file_path = os.path.join(root, file)
            break

# XBRLファイルが見つからない場合のエラーハンドリング
if xbrl_file_path is None:
    raise FileNotFoundError("XBRLファイルが見つかりませんでした。")

# XBRLファイルのバイナリデータを読み込む
with open(xbrl_file_path, 'rb') as file:
    raw_data = file.read()

# エンコーディングを検出
result = chardet.detect(raw_data)
encoding = result['encoding']

# 検出されたエンコーディングを使用してファイルを読み込む
with open(xbrl_file_path, 'r', encoding=encoding) as file:
    xbrl_content = file.read()

# BeautifulSoupでlxmlパーサーを使用して解析
soup = BeautifulSoup(xbrl_content, features="xml")

# 例：特定のタグを取得
elements_revenue = soup.find_all('jpcrp_cor:OperatingRevenue')
elements_profit = soup.find_all('jpcrp_cor:NetIncome')
for element in elements_revenue:
    print(element.text)

for element in elements_profit:
    print(element.text)