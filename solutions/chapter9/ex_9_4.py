class Restaurent() :
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print('The name of the resto is ' + self.restaurant_name )
        print('The type of the resto is ' + self.cuisine_type)
        print('The resto has served  ' + str(self.number_served))

    def open_restaurant(self):
        print(self.restaurant_name + ' restaurent is open')

    def set_number_served(self,number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

resto = Restaurent('pizziara', 'itaian')
print(resto.number_served)
resto.number_served = 12
print(resto.number_served)

resto.set_number_served(17)
print(resto.number_served)

resto.increment_number_served(5)
resto.describe_restaurant()
