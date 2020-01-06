addTopin = True
while addTopin:
    msg = input('Which topping  do you want to add ? ')
    if(msg == 'quit'):
        addTopin = False
        print('No more toppings to add')
    else:
        print('Adding topping ' + msg)
