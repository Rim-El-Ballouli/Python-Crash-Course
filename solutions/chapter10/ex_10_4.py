while True:
    print('enter q to quit qny time ')
    name = input('Enter your name ')
    if name == 'q':
        break
    else:
        print('Hello ' + name)

    with open('guest_book.txt', 'a') as file:
        file.write(name + '\n')