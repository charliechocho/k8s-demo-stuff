import requests

getres = requests.get('http://127.0.0.1:8000/api/v1/users')

res = getres.json()

for item in res:
    print(item)
    