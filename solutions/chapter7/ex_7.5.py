ask_age = True
while ask_age:
    age = int(input('What is your age? '))
    if age == 'quit':
		break
    elif(age < 3):
    	print('Your ticket is free')
    elif(age < 12):
      	print('Your ticket costs 10$')
    else:
    	print('Your ticket costs 15$')
