cities = {
    'paris' :
        {'country' : 'France',
         'population' : '2.141 million',
        'fact': 'There’s only one STOP sign in the entire city of Paris' },
    'london' :
        {'country': 'United Kingdom',
        'population': '8.9 million',
        'fact': 'London is the largest city in the United Kingdom'}
}
for city, info in cities.items():
    print(city)
    for key, value in info.items():
        print(key + ':' + value)

