import json

number = input('Enter your favorite number ')
with open('favorite_number.json', 'w') as file_object:
    json.dump(number, file_object)

with open('favorite_number.json', 'r') as file_object:
    fav_num = json.load(file_object)
    print('I know your favorite number ' + fav_num)
