from uuid import uuid4
import requests
import json

def create_uuid():
    id = uuid4()
    return id

def create_user(id):
    userdict = {}
    userdict["id"] = str(id)
    userdict["first_name"] = input('Enter user first name: ')
    userdict["last_name"] = input('Enter user last name: ')
    userdict["gender"] = input('Enter user gender: ')
    roles = input('Enter role of the user (press enter for "user"): ') or "user"
    userdict["roles"] = [roles]
    
    return json.dumps(userdict)
    
def post_user(user):    
    mkeusr = requests.post('http://158.179.201.65:8080/api/v1/users', data=user)

id = create_uuid()
user = create_user(id)
answ = input('Do you want to create this user(Y/N)? ("Press Enter for Y ") ') or 'y'

if answ.lower() == 'y':
    try:
        post_user(user)
        print('\nExcellent!! You added a new user to the database!')
    except requests.exceptions.ConnectionError as error:
        print(f"Errormessage : {error}\nCan't reach API endpoint!")        
else:
    print('Ok, please run this again if you change your mind!!')


