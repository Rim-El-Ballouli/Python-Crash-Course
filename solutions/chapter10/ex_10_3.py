name = input('Enter your name ')

with open('guest.txt', 'a') as file:
    file.write(name + '\n')