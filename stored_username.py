"""functions that returns username if present else returns None """
import json
import new_username
def get_stored_username():
    file_name = 'username.json'
    with open(file_name) as file_object:
        try:
            username = json.load(file_object)
        except json.decoder.JSONDecodeError:
            username = new_username.get_new_username()
    if username:
        return username
    else:
        return None

