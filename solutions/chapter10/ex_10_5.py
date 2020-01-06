while True:
    print('enter q to quit qny time ')
    name = input('Why do you like programming ')
    if name == 'q':
        break
    with open('programming_lovers.txt', 'a') as file:
        file.write(name + '\n')