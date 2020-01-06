addToping = True
while addToping:
	print('Enter quit to quit')
    msg = input('Which topping do you want to add? ')
    if(msg == 'quit'):
    	addTopin = False
    	print('No more toppings to add')
    else:
    	print('Adding topping ' + msg)

toping = ''
while toping != 'quit':
	print('Enter quit to quit')
    toping = input('Which topping do you want to add? ')
    if toping != 'quit':
    	print('adding toping ' + toping)

while True:
	print('Enter quit to quit')
	toping = input('Which topping do you want to add? ')
	if toping == 'quit':
		break
	else:
    	print('adding toping ' + toping)

