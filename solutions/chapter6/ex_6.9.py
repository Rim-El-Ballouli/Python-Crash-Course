favorite_places = {
    'Eric' : ['Paris', 'London', 'Milano'],
    'Tom' : ['Amsterdam', 'Chicago', 'Zurich'],
    'Ron' : ['Greece', 'Malta', 'Switzerland'],
}

for key, value in favorite_places.items():
    print(key + "'s favorite places are")
    for place in favorite_places[key]:
        print(place)