fav_numbers = {
    'Eric' : [11],
    'Daniel' : [22, 56],
    'Leo' : [44, 23]
}

for name in fav_numbers.keys():
    print(name + "'s favorite numbers are ")
    for item in fav_numbers[name]:
        print(item)