rivers = {
    'nile' : 'egypt',
    'amazon river' : 'America',
    'mississipi river' : 'America'
}

for key, value in rivers.items():
    print('The ' + key.title() + ' runs in ' + value)

for key in rivers.keys():
    print(key.title())

for value in rivers.values():
    print(value)
