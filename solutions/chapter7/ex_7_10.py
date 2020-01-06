answers = {}
while True:
    name = input('What is your name? ')
    place =  input('If you could visit one place in the world, where would you go? ')
    answers[name] = place
    
    cont =  input('Do you want to continue? ')
    if cont == 'no':
        break

for name, place in answers.items():
    print(name + ' wants to visit ' + place)
