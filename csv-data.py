import requests

file_name = input('ファイル名:')
api_key = 'c26a08a3c4b74f3a984699735c5f077f'
url = 'https://api.edinet-fsa.go.jp/api/v2/documents/{}?Subscription-Key={}&type=5'.format(file_name,api_key)

response = requests.get(url)

if response.status_code == 200:
    with open('{}.zip'.format(file_name),'wb') as file:
        file.write(response.content)
    print('ファイルが正常にダウンロードされました')
else:
    print('ファイルのダウンロードに失敗しました\nステータスコード:{}'.format(response.status_code))