import requests

def list_users():
    getres = requests.get('http://127.0.0.1:8000/api/v1/users')
    res = getres.json()
    for item in res:
        print(item.get('id'))
    
def update_user(uid, update):
    useput = requests.put(f'http://127.0.0.1:8000/api/v1/users/{uid}', data=update)

list_users()
update = '{"first_name":"Doug", "last_name":"Dog", "roles":["user"]}'
uid = input('Enter User ID you want to update: ')
update_user(uid, update)

 
