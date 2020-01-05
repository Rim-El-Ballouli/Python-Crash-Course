def city_country(city, country):
    str =  '"' + city.title() + ', ' + country.title() + '"'
    return str

print(city_country('paris', 'france'))