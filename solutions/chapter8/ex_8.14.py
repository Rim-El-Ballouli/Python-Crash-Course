def make_car(manufactor, model, **car):
    car_dictionary = {'manufactor': manufactor, 'model' : model}
    
    for key, value in car.items():
        car_dictionary[key] = value

    return car_dictionary

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)