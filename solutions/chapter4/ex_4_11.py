pizza_names = ["Cheese", "Vegetarian", 'Hawaiian', "Peperoni"]
for pizza_name in pizza_names:
    print('I like ' + pizza_name + 'pizza')
print('I really like pizza!')

friend_pizzas = pizza_names[:]

pizza_names.append('Barbecue')
friend_pizzas.append('Honey Mustard')

print('My friend’s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)

print('My original list of pizzas are:')
for pizza in pizza_names:
    print(pizza)
