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
        
resto1 = Restaurent('pizziara', 'itaian')
resto2 = Restaurent('five guys', 'american')
resto3 = Restaurent('vapiano', 'itaian')

resto1.describe_restaurant()
resto2.describe_restaurant()
resto3.describe_restaurant()
