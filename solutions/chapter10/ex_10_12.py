import json

def get_stored_number():
    filename = 'favorite_number.json'
    try:
        with open(filename) as f_obj:
            fav_num = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return fav_num

def get_new_favorite_number():
    number = input("What is your favorite number? ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
    return number

number = get_stored_number()
if(number == None):
    number = get_new_favorite_number()

print('I know your favorite number ' + number)
