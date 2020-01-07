def city_country(city, country):
    return city.title() + ', ' + country.title()

def city_country_population(city, country, population):
    return  city.title() + ', ' + country.title() + ' - ' + str(population)


def city_country_population_optional(city, country, population=None):
    print(population)
    if population:
        return city.title() + ', ' + country.title() + ' - ' + str(population)
    else:
        return city.title() + ', ' + country.title()
