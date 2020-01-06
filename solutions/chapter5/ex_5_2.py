numbers = ['number1', 'number2', 'number3', 'number4',]


print("\nIs Number1 not my first element in list? I predict False.")
print("Number1" != numbers[0])

print("\nIs Number1 my first element in list? I predict true.")
print("number1" == numbers[0])

print("\nIs Number1 not my first element in list? I predict true.")
print("Number1".lower() != numbers[0])


print("\nIs the size of my list > 7? I predict False.")
print(len(numbers) > 7)

print("\nIs the size of my list == 4? I predict False.")
print(len(numbers) == 10)

print("\nIs the size of my list not = 7? I predict True.")
print(len(numbers) != 7)



print("\nIs my first element and last element eaqual to number1 qnd number5?"
      + "I predict False.")
print(('number1' in numbers) and ('number5' in numbers))

print("\nIs my first element or last element equal to number1 or number5?"
      + "I predict True.")
print(('number1' in numbers) or ('number5' in numbers))




print("\nIs number1 in my list? I predict True.")
print('number1' in numbers)

print("\nIs number6 not in my list? I predict True.")
print('number6' not in numbers)
