import requests

url = 'http://127.0.0.1:5001/create_note'

data = {
    'username':'kk222',
    'title': 'test2',
    'body': 'test2',
    'private': 'False'
}

r = requests.post(url=url, data=data)
print(r.text)
