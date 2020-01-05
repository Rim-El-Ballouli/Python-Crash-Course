class Restaurent() :
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print('The name of the resto is ' + self.restaurant_name )
        print('The type of the resto is ' + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + ' restaurent is open')
        
resto = Restaurent('pizziara', 'itaian')

print(resto.restaurant_name)
print(resto.cuisine_type)

resto.describe_restaurant()
resto.open_restaurant()
