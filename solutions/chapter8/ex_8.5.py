def describe_city(city, country='france'):
    str =  city.title() + ' is in ' + country.title()
    return str

print(describe_city('paris'))
print(describe_city('lyon'))
print(describe_city('milan', 'italy'))