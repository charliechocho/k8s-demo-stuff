import requests
import json

def list_users():
    it_no = 1
    id_list = {}
    getres = requests.get('http://127.0.0.1:8000/api/v1/users')
    res = getres.json()
    for item in res:
        print(f"{it_no}: {item.get('id')}\
        Name: {item.get('first_name')}\
        FamName: {item.get('last_name')}")
        id_list[it_no] = item.get('id')
        it_no += 1
    return id_list

def make_usr_updates():
    userdict = {}
    userdict["first_name"] = input('Enter user first name: ')
    userdict["last_name"] = input('Enter user last name: ') 
    roles = input('Enter role of the user (User or Admin): ')
    userdict["roles"] = [roles]
    
    return json.dumps(userdict)
    
def update_user(uid, update):
    useput = requests.put(f'http://127.0.0.1:8000/api/v1/users/{uid}', data=update)

id_list = list_users()
uid = input('Enter User ID you want to update: ')
update = make_usr_updates()
print(update)
update_user(id_list[int(uid)], update)

 
