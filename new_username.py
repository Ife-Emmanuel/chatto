"""function that stores and returns username of user upon input."""
import json
def get_new_username():
    file_name = 'username.json'
    with open(file_name, 'w') as file_object:
        user_name = input('Enter you name : ')
        json.dump(user_name, file_object)
    return user_name