while True:
    print('To quite enter q')

    num1 = input('Enter the first number ')
    if num1 == 'q':
        break
    num2 = input('Enter the second number ')
    
    if num2 == 'q':
        break
    try:
        number1 = int(num1)
        number2 = int(num2)
    except ValueError: # in python 3.6 the error is Value error noy TypeError as stated in book
        print('Your input must be an integer')
    else:
        print(number1 + number2)