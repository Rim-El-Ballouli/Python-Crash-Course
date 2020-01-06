try:
    with open('cats.txt') as file_object:
        content1 = file_object.read()

    with open('dogs.txt') as file_object:
        content2 = file_object.read()

except FileNotFoundError:
    print('The file is not found')
else:
    print(content1)
    print(content2)