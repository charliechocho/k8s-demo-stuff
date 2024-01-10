from uuid import uuid4
import requests

def create_uuid():
    id = uuid4()
    return str(id)

def create_user():
    userdict = {}
    userdict["first_name"] = input('Enter user first name: ')
    userdict["last_name"] = input('Enter user last name: ')
    userdict["gender"] = input('Enter user gender: ')
    roles = input('Enter role of the user (press enter for "user"): ') or "user"
    userdict["roles"] = [roles]
    
    return str(userdict)
    
def post_user(user):    
    mkeusr = requests.post('http://127.0.0.1:8000/api/v1/users', json=user)

id = create_uuid()
user = create_user()
answ = input('Do you want to create this user(Y/N)? ("Press Enter for Y ")') or 'y'

# print(f"'{user}'")
if answ.lower() == 'y':
    try:
        post_user(f"'{user}'")
    except requests.exceptions.ConnectionError as error:
        print(f"Errormessage : {error}\nCan't reach API endpoint!")        
else:
    print('Ok, please run this again if you change your mind!!')


